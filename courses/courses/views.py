from rest_framework import viewsets
from django.http import JsonResponse
from .models import Course,Lesson,Assessment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CourseSerializer,AssessmentSerializer,LessonSerializer
from .models import Course, Lesson, Assessment
from .serializers import CourseSerializer, LessonSerializer, AssessmentSerializer


@api_view(['GET','POST'])
def course_list(request):
    print(request.method)
    if request.method == 'GET':
        courses=Course.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return JsonResponse({"courses":serializer.data})
    
@api_view(['GET','POST'])
def lesson_list(request):
    print(request.method)
    if request.method == 'GET':
        lessons=Lesson.objects.all()
        serializer=LessonSerializer(lessons,many=True)
        return JsonResponse({"lessons":serializer.data})
    
@api_view(['GET','POST'])
def assessment_list(request):
    print(request.method)
    if request.method == 'GET':
        assessments=Assessment.objects.all()
        serializer=AssessmentSerializer(assessments,many=True)
        return JsonResponse({"assessments":serializer.data})