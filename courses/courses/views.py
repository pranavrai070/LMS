from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, Lesson, Assessment
from .serializers import CourseSerializer, LessonSerializer, AssessmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

@api_view(['GET','POST'])
def drink_list(request):
    print(request.method)
    return JsonResponse({"Successfully hitting the Courses Route":"True"})