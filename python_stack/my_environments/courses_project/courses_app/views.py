from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course, Description

# 1. عرض الصفحة الرئيسية التي تحتوي على الفورم والجدول معاً
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

# 2. استقبال البيانات والتحقق منها ثم حفظها في الجدولين المترابطين
def create(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        # إنشاء الكورس أولاً
        new_course = Course.objects.create(name=request.POST['name'])
        # إنشاء الوصف المرتبط بالكورس (One-to-One)
        Description.objects.create(course=new_course, content=request.POST['description'])
        
        return redirect('/')
    return redirect('/')

# 3. عرض صفحة التأكيد "Are you sure you want to delete...؟"
def confirm_delete(request, id):
    context = {
        'course': get_object_or_404(Course, id=id)
    }
    return render(request, 'delete.html', context)

# 4. تنفيذ الحذف النهائي عند الضغط على "Yes" والتوجيه للرئيسية
def destroy(request, id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=id)
        course.delete() # سيقوم بحذف الوصف تلقائياً بسبب CASCADE
    return redirect('/')