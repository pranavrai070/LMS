from django.db import models
from students.models import Student

class Message(models.Model):
    sender = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="sent_messages")