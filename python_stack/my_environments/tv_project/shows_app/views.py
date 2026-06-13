from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Show

def root(request):
    return redirect('/shows')

def index(request):
    context = { 'shows': Show.objects.all() }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

# تعديل دالة الإنشاء لتشمل التحقق
def create(request):
    if request.method == 'POST':
        # تمرير بيانات الفورم للمانجر
        errors = Show.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new') # إعادة التوجيه لصفحة الإضافة لعرض الأخطاء
        
        # إذا لم تكن هناك أخطاء، يتم الإنشاء بنجاح
        new_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        return redirect(f'/shows/{new_show.id}')
    return redirect('/shows/new')

def show_detail(request, id):
    context = { 'show': get_object_or_404(Show, id=id) }
    return render(request, 'show_detail.html', context)

def edit(request, id):
    context = { 'show': get_object_or_404(Show, id=id) }
    return render(request, 'edit.html', context)

# تعديل دالة التحديث لتشمل التحقق
def update(request, id):
    if request.method == 'POST':
        # نمرر الـ id هنا لاستثنائه من شرط التكرار (Unique)
        errors = Show.objects.basic_validator(request.POST, show_id=id)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{id}/edit')
        
        show = get_object_or_404(Show, id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{show.id}')
    return redirect(f'/shows/{id}/edit')

def destroy(request, id):
    if request.method == 'POST':
        show = get_object_or_404(Show, id=id)
        show.delete()
    return redirect('/shows')