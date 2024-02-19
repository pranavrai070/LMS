Course Management Module:

Django models for courses, lessons, and assessments.
APIs for creating, organizing, and managing course content.
Scheduler for lesson and assessment scheduling.
Student Engagement Module:

User authentication and registration.
APIs for students to access course materials and participate in discussions.
Interactive tools API for quizzes, assignments, and collaborative projects.
Analytics and Reporting Module:

Django models to store user activity, course performance, and student progress.
APIs for generating comprehensive analytics and reports.
Communication and Collaboration Module:

Real-time messaging API.
Discussion forum API.
APIs for live session management.
APIs for group projects and peer-to-peer interaction.
Content Repository Module:

run the command in terminal : python manage.py runserver 
if you want to run the server on a specific port then just write : python manage.py runserver 9005
9005 is your port

Added Features: routes added to GET and POST of courses,lessons,assessments (e.g:http://127.0.0.1:8000/courses/,assessments,lessons).
You can also access admin route : http://127.0.0.1:8000/admin/
Do pip install packagename for any package


Django models for storing and organizing educational resources.
APIs for searching, categorization, and accessing resources.



Routes working till Now:
    'courses/'  --GET,POST
    'lessons/<int:course_id>/'  --GET
    'assessments/<int:course_id>' --GET
    'activities/<int:lesson_id>' --GET
    'questions/<int:assesment_id>' --GET
    'users/' --GET
    'login/' --POST
    'get_course_analytics/'  --GET
    'get_lesson_analytics/'  --GET
    'update_progress/'  --POST
    'send_message/'  --POST
    'get_messages/'  --GET

All the requirements and modules are completed


another Admin Credentials added:
 username: admin
 password: password


COMMAND TO START THE BACKEND SERVER
1. Using Terminal move to the courses directory where manage.py file is present
2. run the command : python manage.py runserver 8000 to run the project on 8000 PORT 
3. visit http://127.0.0.1:8000/admin/ , you will see admin dashboard for login 
4. Admin Credentials:
 username: admin
 password: password
5. you can control your backend from dashboard.
