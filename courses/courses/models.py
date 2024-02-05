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
    title = models.CharField(max_length=255)
    questions = models.TextField()

    def __str__(self):
        return self.title
    
class Activities(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
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
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_name = models.ForeignKey(Users, on_delete=models.CASCADE)
    progressPercentage=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.progressPercentage
    
class tr_user_login_token(models.Model):
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE)
    token=models.CharField(max_length=255)
    dtti_expiry=models.DateTimeField()
    dtti_logout=models.DateTimeField(null=True,blank=True)
    dtti_created=models.DateTimeField(auto_now_add=True)
    dtti_updated=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.token



    
    

    

    
