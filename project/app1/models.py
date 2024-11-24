from django.db import models

# Create your models here.

class table(models.Model):
    name=models.CharField(max_length=30)
    mn=models.IntegerField()
    address=models.CharField(max_length=50)
    email=models.EmailField()
    feedback = models.CharField(max_length=255, default="Default Feedback")
