from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255, default="I would like to register for a course")
    phone = models.CharField(max_length=255)
    course = models.ForeignKey('core.Course', on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + " - " + self.created_at.strftime("%d/%m/%Y %H:%M")

class Course(models.Model):

    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class MailingList(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + " - " + self.created_at.strftime("%d/%m/%Y %H:%M")