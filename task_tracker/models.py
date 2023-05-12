from django.db import models

# Create your models here.



class Task(models.Model):
    task=models.CharField(max_length=40 )
    day=models.CharField(max_length=40)
    
    
    
    def __str__(self):
        
        return self.task
