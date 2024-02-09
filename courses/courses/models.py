from django.db import models
from django.contrib.postgres.fields import ArrayField


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Assessment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField('Question')

    def __str__(self):
        return self.title
    
class Activities(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE,default=1)  
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Info(models.Model):
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=10000)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Question(models.Model):
    question=models.CharField(max_length=1000)
    assesment=models.ForeignKey(Assessment, on_delete=models.CASCADE,default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    options= models.CharField(max_length=1000)
    answer = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.question
    
    
class Users(models.Model):
    user_name = models.CharField(max_length=255)
    full_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=15)
    birthDate = models.DateField()
    user_type = models.CharField(max_length=255)
    courses=models.CharField(max_length=255,default='')
    lessons=models.CharField(max_length=255,default='')
    assessments=models.CharField(max_length=255,default='')
    activities=models.CharField(max_length=255,default='')
    dtti_created = models.DateTimeField(auto_now_add=True)
    dtti_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user_name
    
class student_progress(models.Model):
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    lessons = models.ManyToManyField('Lesson')
    assessments = models.ManyToManyField('Assessment')
    ativities = models.ManyToManyField('Activities')
    courses= models.ManyToManyField('Course')

    def __str__(self):
        return self.student
    

class StudentLessonProgress(models.Model):
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class StudentActivityProgress(models.Model):
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class StudentAssessmentProgress(models.Model):
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class StudentInfoProgress(models.Model):
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
 
class tr_user_login_token(models.Model):
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE)
    token=models.CharField(max_length=255)
    dtti_expiry=models.DateTimeField()
    dtti_logout=models.DateTimeField(null=True,blank=True)
    dtti_created=models.DateTimeField(auto_now_add=True)
    dtti_updated=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.token



    
    

    

    
