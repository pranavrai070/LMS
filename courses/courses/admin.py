from django.contrib import admin
from .models import Course,Lesson,Assessment,Activities,Users,student_progress

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Assessment)
admin.site.register(Activities)
admin.site.register(Users)
admin.site.register(student_progress)