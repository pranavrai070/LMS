from django.contrib import admin
from .models import Course,Lesson,Assessment,Activities,Question,Users,tr_user_login_token,StudentLessonProgress,StudentInfoProgress,StudentActivityProgress,StudentAssessmentProgress,Info

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Assessment)
admin.site.register(Activities)
admin.site.register(Users)
admin.site.register(StudentAssessmentProgress)
admin.site.register(StudentActivityProgress)
admin.site.register(StudentLessonProgress)
admin.site.register(StudentInfoProgress)
admin.site.register(Info)
admin.site.register(Question)
admin.site.register(tr_user_login_token)