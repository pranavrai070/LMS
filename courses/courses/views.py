from rest_framework import viewsets
from django.http import JsonResponse
from .models import Course,Lesson,Assessment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from .serializers import CourseSerializer,AssessmentSerializer,LessonSerializer
from .models import Course, Lesson, Assessment,Activities,Users,student_progress,tr_user_login_token
from .serializers import CourseSerializer, LessonSerializer, AssessmentSerializer,ActivitiesSerializer,UsersSerializer,student_progressSerializer,tr_user_login_token_Serializer
import secrets


@csrf_exempt
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
    
@csrf_exempt    
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
    
@csrf_exempt    
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
        
@csrf_exempt
@api_view(['GET','POST'])
def activities(request):
    print(request.method)
    if request.method == 'GET':
        activities=Activities.objects.all()
        serializer=ActivitiesSerializer(activities,many=True)
        return JsonResponse({"activities":serializer.data})
    if(request.method=='POST'):
        print(request.data)
        serializer=ActivitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Data is Not Validated"},status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET','POST'])
def users(request):
    print(request.method)
    if request.method == 'GET':
        users=Users.objects.all()
        serializer=UsersSerializer(users,many=True)
        return JsonResponse({"users":serializer.data})
    if(request.method=='POST'):
        print(request.data)
        serializer=UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Data is Not Validated"},status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET','POST'])
def student_progress_route(request):
    print(request.method)
    if request.method == 'GET':
        Student_progress=student_progress.objects.all()
        serializer=student_progressSerializer(Student_progress,many=True)
        return JsonResponse({"student_progress":serializer.data})
    if(request.method=='POST'):
        print(request.data)
        serializer=student_progressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Data is Not Validated"},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt       
@api_view(['GET','POST'])
def login(request):
    print(request.method)
    if request.method == 'GET':
        return Response({"message":"GET request Method is Not Allowed on this route"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if(request.method=='POST'):
        print('printing incoming data')
        users=Users.objects.all()
        serializer=UsersSerializer(users,many=True) 
        print('serializer_data got printing')
        print(serializer.data)
        print(request.data)
        incoming_data = request.data
        for user_data in users:
            if (
                incoming_data['in_login_id'] == user_data.user_name or
                incoming_data['in_login_id'] == user_data.email or
                incoming_data['in_login_id'] == user_data.mobile
            ):
                def custom_check_password(raw_password, stored_password):
                    # Check if the raw_password matches the stored password
                    return raw_password == stored_password
                # Match found, check password
                if custom_check_password(incoming_data['in_password'], user_data.password):
                    # Password is correct, return response with token and user_id
                    def generate_random_token():
                        # Generate a random token with 32 characters
                        return secrets.token_hex(16)
                    random_token = generate_random_token()
                    # Check if there is an existing token with dtti_logout as null
                    existing_token = tr_user_login_token.objects.filter(user_id=user_data.id, dtti_logout__isnull=True).first()
                    print('existing_toke',existing_token)

                    if existing_token:
                        # If an existing token is found, update dtti_logout and dtti_updated
                        existing_token.dtti_logout = timezone.now()
                        existing_token.dtti_updated = timezone.now()
                        existing_token.save()
                        new_token = tr_user_login_token(
                            user_id=user_data.id,
                            token=random_token,
                            dtti_expiry=timezone.now() + timedelta(hours=6)
                        )
                        new_token.save()
                    else:
                        # Add a new token for the user with dtti_expiry 6hrs plus from now
                        new_token = tr_user_login_token(
                            user_id=user_data.id,
                            token=random_token,
                            dtti_expiry=timezone.now() + timedelta(hours=6)
                        )
                        new_token.save()
                    return JsonResponse({"message": "Login successful", "token": random_token, "user_id": user_data.id,"user_type":user_data.user_type})
                else:
                    # Password is incorrect, return response
                    print('getting password compare')
                    print(type(incoming_data['in_password']))
                    print(type(user_data.password))
                    return JsonResponse({"message": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # No match found, return response
        return JsonResponse({"message": "Invalid username"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "GET request Method is Not Allowed on this route"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        