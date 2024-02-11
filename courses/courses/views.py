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
from .models import Course, Lesson, Assessment,Activities,Users,Message,Question,student_progress,tr_user_login_token,StudentActivityProgress,StudentAssessmentProgress,StudentInfoProgress,Info,StudentLessonProgress
from .serializers import CourseSerializer, LessonSerializer,MessageSerializer, AssessmentSerializer,ActivitiesSerializer,UsersSerializer,QuestionsSerializer,student_progressSerializer,tr_user_login_token_Serializer,StudentActivityProgressSerializer,StudentLessonProgressSerializer,StudentInfoProgressSerializer,InfoSerializer
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
def lesson_list(request,course_id):
    print(request.method)
    if request.method == 'GET':
        # course_id=1
        print('printing course id parameter')
        print(course_id)
        lessons=Lesson.objects.filter(course=course_id)
        serializer=LessonSerializer(lessons,many=True)
        print(serializer.data)
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
def assessment_list(request,lesson_id):
    print(request.method)
    if request.method == 'GET':
        assessments=Assessment.objects.filter(lesson=lesson_id)
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
def activities(request,lesson_id):
    print(request.method)
    if request.method == 'GET':
        activities=Activities.objects.filter(lesson=lesson_id)
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
def questions(request,assesment_id):
    print(request.method)
    if request.method == 'GET':
        questions=Question.objects.filter(assesment=assesment_id)
        serializer=QuestionsSerializer(questions,many=True)
        return JsonResponse({"questions":serializer.data})
    if(request.method=='POST'):
        print(request.data)
        serializer=QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Data is Not Validated"},status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET','POST'])
def send_message(request):
    sender_id = request.data['sender']
    receiver_id = request.data['receiver_id']
    subject = request.data['subject']
    content = request.data['content']

    if not (receiver_id and subject and content):
        return JsonResponse({'error': 'Receiver ID, subject, and content are required'}, status=400)

    try:
        receiver = Users.objects.get(pk=receiver_id)
        sender=Users.objects.get(pk=sender_id)
        message = Message.objects.create(sender=sender, receiver=receiver, subject=subject, content=content)
        return JsonResponse({'message_id': message.id}, status=201)
    except Users.DoesNotExist:
        return JsonResponse({'error': 'Receiver not found'}, status=404)
    

@csrf_exempt
@api_view(['GET','POST']) 
def get_messages(request):
    print("getting message route hit")
    print(request)
    user = request.data['user']
    messages_sent = Message.objects.filter(sender=user)
    messages_received = Message.objects.filter(receiver=user)

    sent_messages_data = [{'id': msg.id,  'subject': msg.subject, 'content': msg.content, 'timestamp': msg.timestamp} for msg in messages_sent]
    received_messages_data = [{'id': msg.id, 'subject': msg.subject, 'content': msg.content, 'timestamp': msg.timestamp, 'is_read': msg.is_read} for msg in messages_received]

    return JsonResponse({'sent_messages': sent_messages_data, 'received_messages': received_messages_data})
        

@csrf_exempt
@api_view(['GET','POST'])   
def update_progress(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        lesson_id = request.POST.get('lesson_id')
        activity_id = request.POST.get('activity_id')
        assessment_id = request.POST.get('assessment_id')
        info_id = request.POST.get('info_id')

        if not (student_id and lesson_id and (activity_id or assessment_id or info_id)):
            return JsonResponse({'error': 'Student ID, lesson ID, and either activity ID, assessment ID, or info ID are required'}, status=400)

        # Update student progress based on the provided IDs
        # Example logic: Mark activity/assessment/info as completed for the student

        if activity_id:
            try:
                activity = Activities.objects.get(pk=activity_id, lesson_id=lesson_id)
                StudentActivityProgress.objects.update_or_create(student_id=student_id, activity=activity, defaults={'completed': True})
                return JsonResponse({'success': 'Activity progress updated successfully'})
            except Activities.DoesNotExist:
                return JsonResponse({'error': 'Activity not found'}, status=404)

        elif assessment_id:
            try:
                assessment = Assessment.objects.get(pk=assessment_id, lesson_id=lesson_id)
                StudentAssessmentProgress.objects.update_or_create(student_id=student_id, assessment=assessment, defaults={'completed': True})
                return JsonResponse({'success': 'Assessment progress updated successfully'})
            except Assessment.DoesNotExist:
                return JsonResponse({'error': 'Assessment not found'}, status=404)

        elif info_id:
            try:
                info = Info.objects.get(pk=info_id, lesson_id=lesson_id)
                StudentInfoProgress.objects.update_or_create(student_id=student_id, info=info, defaults={'completed': True})
                return JsonResponse({'success': 'Info progress updated successfully'})
            except Info.DoesNotExist:
                return JsonResponse({'error': 'Info not found'}, status=404)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    

@csrf_exempt
@api_view(['GET','POST'])  
def get_course_analytics(request):
    courses = Course.objects.all()
    course_analytics = []

    for course in courses:
        total_lessons = course.lesson_set.count()
        completed_lessons = StudentLessonProgress.objects.filter(lesson__course=course, student_id=1, completed=True).count()
        course_completion_percentage = (completed_lessons / total_lessons) * 100 if total_lessons != 0 else 0

        course_analytics.append({
            'course_title': course.title,
            'course_completion_percentage': course_completion_percentage,
            'completed_lessons': completed_lessons,
            'total_lessons': total_lessons,
        })

    return JsonResponse(course_analytics, safe=False)


@csrf_exempt
@api_view(['GET','POST'])  
def get_lesson_analytics(request):
    lessons = Lesson.objects.filter(course_id=1)
    lesson_analytics = []

    for lesson in lessons:
        total_sections = (
            lesson.activities_set.count() +
            lesson.assessment_set.count() +
            lesson.info_set.count()
        )

        completed_sections = (
            StudentActivityProgress.objects.filter(activity__lesson=lesson, student_id=1, completed=True).count() +
            StudentAssessmentProgress.objects.filter(assessment__lesson=lesson, student_id=1, completed=True).count() +
            StudentInfoProgress.objects.filter(info__lesson=lesson, student_id=1, completed=True).count()
        )

        lesson_completion_percentage = (completed_sections / total_sections) * 100 if total_sections != 0 else 0

        lesson_analytics.append({
            'lesson_title': lesson.title,
            'lesson_completion_percentage': lesson_completion_percentage,
            'completed_sections': completed_sections,
            'total_sections': total_sections,
        })

    return JsonResponse(lesson_analytics, safe=False)

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
                    user_instance = Users.objects.get(id=user_data.id)

                    if existing_token:
                        # If an existing token is found, update dtti_logout and dtti_updated
                        existing_token.dtti_logout = timezone.now()
                        existing_token.dtti_updated = timezone.now()
                        existing_token.save()
                        new_token = tr_user_login_token(
                            user_id=user_instance,
                            token=random_token,
                            dtti_expiry=timezone.now() + timedelta(hours=6)
                        )
                        new_token.save()
                    else:
                        # Add a new token for the user with dtti_expiry 6hrs plus from now
                        new_token = tr_user_login_token(
                            user_id=user_instance,
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
        