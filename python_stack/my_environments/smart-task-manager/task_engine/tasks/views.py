import json
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Category, Task, TaskAssignment, TaskCategory, User


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------

def auth_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'login':
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            messages.error(request, 'Invalid username or password.')
            return render(request, 'auth.html', {'form_mode': 'login'})

        if action == 'register':
            username = request.POST.get('username', '').strip()
            email = request.POST.get('email', '').strip()
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')

            if not username or not email or not password1:
                messages.error(request, 'All fields are required.')
                return render(request, 'auth.html', {'form_mode': 'register'})

            if password1 != password2:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'auth.html', {'form_mode': 'register'})

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken.')
                return render(request, 'auth.html', {'form_mode': 'register'})

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
                return render(request, 'auth.html', {'form_mode': 'register'})

            user = User.objects.create_user(username=username, email=email, password=password1)
            _send_welcome_email(user)
            login(request, user)
            return redirect('dashboard')

    return render(request, 'auth.html', {'form_mode': 'login'})


def logout_view(request):
    logout(request)
    return redirect('auth')


def _send_welcome_email(user):
    body = render_to_string('emails/welcome_email.html', {'user': user})
    send_mail(
        subject='Welcome to Smart Task Manager!',
        message='',
        from_email=None,
        recipient_list=[user.email],
        html_message=body,
        fail_silently=True,
    )


# ---------------------------------------------------------------------------
# Dashboard
# ---------------------------------------------------------------------------

@login_required(login_url='/')
def dashboard_view(request):
    now = timezone.now()
    deadline_threshold = now + timedelta(days=7)

    total_tasks = Task.objects.filter(user=request.user).count()
    in_progress = Task.objects.filter(user=request.user, status=Task.STATUS_IN_PROGRESS).count()
    completed = Task.objects.filter(user=request.user, status=Task.STATUS_COMPLETED).count()
    pending = Task.objects.filter(user=request.user, status=Task.STATUS_PENDING).count()

    upcoming = (
        Task.objects.filter(
            user=request.user,
            due_date__range=(now, deadline_threshold),
        )
        .exclude(status=Task.STATUS_COMPLETED)
        .order_by('due_date')
    )

    upcoming_with_days = [
        {'task': t, 'days_left': (t.due_date - now).days}
        for t in upcoming
    ]

    context = {
        'total_tasks': total_tasks,
        'in_progress': in_progress,
        'completed': completed,
        'pending': pending,
        'upcoming_with_days': upcoming_with_days,
        'now': now,
    }
    return render(request, 'dashboard.html', context)


# ---------------------------------------------------------------------------
# Task workspace — HTML view
# ---------------------------------------------------------------------------

@login_required(login_url='/')
def tasks_view(request):
    categories = Category.objects.all()
    tasks = (
        Task.objects.filter(user=request.user)
        .prefetch_related('task_categories__category', 'assignments')
        .order_by('due_date')
    )
    context = {'tasks': tasks, 'categories': categories}
    return render(request, 'tasks.html', context)


# ---------------------------------------------------------------------------
# AJAX — Task CRUD
# ---------------------------------------------------------------------------

@login_required(login_url='/')
@require_POST
def task_create(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON.'}, status=400)

    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    due_date = data.get('due_date', '').strip()
    category_ids = data.get('categories', [])

    if not title:
        return JsonResponse({'error': 'Title is required.'}, status=400)
    if not due_date:
        return JsonResponse({'error': 'Due date is required.'}, status=400)

    task = Task.objects.create(
        title=title,
        description=description or None,
        due_date=due_date,
        status=Task.STATUS_PENDING,
        user=request.user,
    )

    for cid in category_ids:
        try:
            cat = Category.objects.get(pk=int(cid))
            TaskCategory.objects.create(task=task, category=cat)
        except (Category.DoesNotExist, ValueError):
            pass

    return JsonResponse({'success': True, 'task': _task_to_dict(task)}, status=201)


@login_required(login_url='/')
@require_POST
def task_update_status(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON.'}, status=400)

    new_status = data.get('status', '').strip()
    valid = {Task.STATUS_PENDING, Task.STATUS_IN_PROGRESS, Task.STATUS_COMPLETED}
    if new_status not in valid:
        return JsonResponse({'error': f'Invalid status. Choose from: {", ".join(valid)}'}, status=400)

    task.status = new_status
    task.save(update_fields=['status'])
    return JsonResponse({'success': True, 'task': _task_to_dict(task)})


@login_required(login_url='/')
@require_POST
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON.'}, status=400)

    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    due_date = data.get('due_date', '').strip()
    category_ids = data.get('categories', [])

    if not title:
        return JsonResponse({'error': 'Title is required.'}, status=400)
    if not due_date:
        return JsonResponse({'error': 'Due date is required.'}, status=400)

    task.title = title
    task.description = description or None
    task.due_date = due_date
    task.save(update_fields=['title', 'description', 'due_date'])

    TaskCategory.objects.filter(task=task).delete()
    for cid in category_ids:
        try:
            cat = Category.objects.get(pk=int(cid))
            TaskCategory.objects.create(task=task, category=cat)
        except (Category.DoesNotExist, ValueError):
            pass

    return JsonResponse({'success': True, 'task': _task_to_dict(task)})


@login_required(login_url='/')
@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return JsonResponse({'success': True})


@login_required(login_url='/')
def task_list_json(request):
    status_filter = request.GET.get('status', '').strip()
    qs = Task.objects.filter(user=request.user).prefetch_related('task_categories__category')
    if status_filter in {Task.STATUS_PENDING, Task.STATUS_IN_PROGRESS, Task.STATUS_COMPLETED}:
        qs = qs.filter(status=status_filter)
    return JsonResponse({'tasks': [_task_to_dict(t) for t in qs.order_by('due_date')]})


def _task_to_dict(task):
    cats = [tc.category.name for tc in task.task_categories.select_related('category').all()]
    return {
        'id': task.pk,
        'title': task.title,
        'description': task.description or '',
        'due_date': task.due_date if isinstance(task.due_date, str) else (task.due_date.strftime('%Y-%m-%dT%H:%M') if task.due_date else ''),
        'status': task.status,
        'categories': cats,
    }


# ---------------------------------------------------------------------------
# About
# ---------------------------------------------------------------------------

def about_view(request):
    return render(request, 'about.html')
