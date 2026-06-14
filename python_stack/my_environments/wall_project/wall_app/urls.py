from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall_index),                    # الصفحة الرئيسية للحائط
    path('post_message', views.post_message),      # نشر رسالة
    path('post_comment/<int:msg_id>', views.post_comment), # إضافة تعليق
    path('delete_message/<int:msg_id>', views.delete_message), # حذف منشور (Bonus)
]