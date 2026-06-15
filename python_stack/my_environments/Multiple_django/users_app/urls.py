from django.urls import path
from . import views

urlpatterns = [
    # شاشات الدخول والترحيب
    path('', views.signin_page),
    path('signin', views.signin_page),
    path('register', views.register_page),
    path('logout', views.logout),
    
    # العمليات الخلفية (POST)
    path('process_login', views.process_login),
    path('process_registration', views.process_registration),
    
    # لوحات التحكم (Dashboards)
    path('dashboard', views.dashboard),
    path('dashboard/admin', views.admin_dashboard),
    
    # إدارة المستخدمين (للإدمن)
    path('users/new', views.add_user_page),
    path('users/create', views.process_add_user),
    path('users/remove/<int:user_id>', views.delete_user),
    
    # شاشات الملف الشخصي والتعديل
    path('users/show/<int:user_id>', views.show_user_profile),
    path('users/edit/<int:user_id>', views.edit_user_page),
    path('users/edit/info/<int:user_id>', views.process_edit_info),
    path('users/edit/password/<int:user_id>', views.process_edit_password),
    path('users/edit/description/<int:user_id>', views.process_edit_description),
    
    # نظام الجدار والرسائل (Wall)
    path('post_message/<int:receiver_id>', views.post_message),
    path('post_comment/<int:message_id>', views.post_comment),
]