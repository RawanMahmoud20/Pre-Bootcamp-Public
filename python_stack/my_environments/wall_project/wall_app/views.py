from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import User
from .models import Message, Comment
from django.utils import timezone
from datetime import timedelta

def wall_index(request):
    # حماية المسار من التصفح العشوائي بالـ GET للمستخدمين غير المسجلين
    if 'user_id' not in request.session:
        return redirect('/')
        
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'all_messages': Message.objects.all().order_by('-created_at') # الترتيب التنازلي (الأحدث بالأعلى)
    }
    return render(request, 'wall.html', context)

def post_message(request):
    if request.method == "POST":
        if len(request.POST['message_text'].strip()) > 0:
            Message.objects.create(
                message=request.POST['message_text'],
                user_id=request.session['user_id']
            )
    return redirect('/wall/')

def post_comment(request, msg_id):
    if request.method == "POST":
        if len(request.POST['comment_text'].strip()) > 0:
            Comment.objects.create(
                comment=request.POST['comment_text'],
                user_id=request.session['user_id'],
                message_id=msg_id
            )
    return redirect('/wall/')

def delete_message(request, msg_id):
    message = Message.objects.get(id=msg_id)
    # التحقق أن من يحذف هو المالك والمنشور لم يمر عليه 30 دقيقة (Sensei Bonus)
    if message.user.id == request.session['user_id']:
        time_elapsed = timezone.now() - message.created_at
        if time_elapsed < timedelta(minutes=30):
            message.delete()
        else:
            messages.error(request, "You can only delete your message within 30 minutes of creation.")
    return redirect('/wall/')