from rest_framework import viewsets
from django.http import JsonResponse
from .models import Course,Lesson,Assessment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
    if(request.method=='POST'):
        print(request.data)
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Data is Not Validated"},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def lesson_list(request):
    print(request.method)
    if request.method == 'GET':
        lessons=Lesson.objects.all()
        serializer=LessonSerializer(lessons,many=True)
        return JsonResponse({"lessons":serializer.data})
    if(request.method=='POST'):
        print(request.data)
        serializer=LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Data is Not Validated"},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def assessment_list(request):
    print(request.method)
    if request.method == 'GET':
        assessments=Assessment.objects.all()
        serializer=AssessmentSerializer(assessments,many=True)
        return JsonResponse({"assessments":serializer.data})
    if(request.method=='POST'):
        print(request.data)
        serializer=AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Data is Not Validated"},status=status.HTTP_400_BAD_REQUEST)