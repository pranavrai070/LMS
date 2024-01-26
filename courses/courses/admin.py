from django.contrib import admin
from .models import Course,Lesson,Assessment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Assessment)