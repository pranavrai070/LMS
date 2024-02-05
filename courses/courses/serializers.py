from rest_framework import serializers
from .models import Course, Lesson, Assessment,Activities,Users,student_progress,tr_user_login_token

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

