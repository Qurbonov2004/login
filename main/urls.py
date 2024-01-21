from django.urls import path
from .views import *

urlpatterns=[
    path('main',main,name='main'),

    #sashboard

    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/body/body_create',body_create,name='body_create'),
    path('dashboard/body/body',body,name='body'),
    path('dashboard/body/body_update',body_update,name='body_update'),
    path('dashboard/body/body_delete',body_delete,name='body_delete'),
    #class
    path('dashboard/class/class_create',class_create,name='class_create'),
    path('dashboard/class/classes',classes,name='classes'),
    path('dashboard/class/class_update',class_update,name='class_update'),
    path('dashboard/class/class_delete',class_delete,name='class_delete'),
    #teacher
    path('dashboard/teacher/teacher_create',teacher_create,name='teacher_create'),
    path('dashboard/teacher/teachers',teachers,name='teacher'),
    path('dashboard/teacher/teacher_update',    teacher_update,name='teacher_update'),
    path('dashboard/teacher/teacher_delete',teacher_delete,name='teacher_delete'),
    #service
    path('dashboard/service/service_create',service_create,name='service_create'),
    path('dashboard/service/services',services,name='services'),
    path('dashboard/service/service_update',service_update,name='service_update'),
    path('dashboard/service/service_delete',service_delete,name='service_delete'),
   path('dashboard/auth/register',register_user,name='register_user'),
   path('dashboard/auth/login',login_user,name='login_user'),

] 