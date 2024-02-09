from rest_framework import serializers
from .models import Course, Lesson, Assessment,Activities,Question,Users,student_progress,tr_user_login_token,StudentActivityProgress,StudentInfoProgress,StudentLessonProgress,Info

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class StudentLessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLessonProgress
        fields = '__all__'

class StudentInfoProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfoProgress
        fields = '__all__'

class StudentActivityProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentActivityProgress
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class student_progressSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_progress
        fields = '__all__'

class tr_user_login_token_Serializer(serializers.ModelSerializer):
    class Meta:
        model = tr_user_login_token
        fields = '__all__'

