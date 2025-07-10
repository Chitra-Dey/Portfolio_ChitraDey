from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
#resume ,skill   #project

class Project(models.Model):
    title = models.CharField(max_length=300) 
    description = models.TextField()
    date_added=models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.title}"
class Skill(models.Model):
    subject = models.CharField(max_length=100)
    marks=models.DecimalField(max_digits=5, decimal_places=2)
      
    def __str__(self):
        return f"{self.subject} - {self.marks}"  