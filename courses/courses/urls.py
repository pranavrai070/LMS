"""
URL configuration for courses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', views.course_list),
    path('lessons/<int:course_id>/', views.lesson_list),
    path('assessments/<int:lesson_id>', views.assessment_list),
    path('activities/<int:lesson_id>', views.activities),
    path('questions/<int:assesment_id>', views.questions),
    path('users/', views.users),
    path('get_messages/', views.get_messages),
    path('send_message/', views.send_message),
    path('update_progress/', views.update_progress),
    path('get_lesson_analytics/', views.get_lesson_analytics),
    path('get_course_analytics/', views.get_course_analytics),
    path('student_progress/', views.student_progress_route),
    path('login/', views.login),
]
