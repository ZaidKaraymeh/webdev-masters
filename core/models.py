from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    description = models.TextField(max_length=4000, null=True)
    phone = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + " - " + self.created_at.strftime("%d/%m/%Y %H:%M")

class Course(models.Model):

    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, null=True)
    image = models.ImageField(upload_to='courses', null=True)

    hook = models.CharField(max_length=255, null=True)
    description = RichTextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    duration = models.CharField(max_length=255, null=True)
    # start_date = models.DateField()
    # end_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    number_of_lessons = models.IntegerField(default=0)

    end_of_course_objectives = RichTextField(null=True)
    skills_you_will_learn = RichTextField(null=True)
    who_this_course_is_for = models.TextField(null=True)
    requirements = models.TextField(null=True)

    units = models.ManyToManyField('core.Unit', blank=True)

    discount = models.IntegerField(default=0)
    discount_price = models.DecimalField(max_digits=6, decimal_places=3, default=0)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=255)

    topics = models.ManyToManyField('core.Topic', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class GlobalConfig(models.Model):
    discount = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MailingList(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + " - " + self.created_at.strftime("%d/%m/%Y %H:%M")

class CourseRegistration(models.Model):
    course = models.ForeignKey('core.Course', on_delete=models.CASCADE)
    
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + " - " + self.created_at.strftime("%d/%m/%Y %H:%M")
    
class BundleRegistration(models.Model):
    bundle = models.ForeignKey('core.Bundle', on_delete=models.CASCADE)
    
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + " - " + self.created_at.strftime("%d/%m/%Y %H:%M")



class Bundle(models.Model):
    courses = models.ManyToManyField('core.Course', blank=True)

    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, null=True)
    image = models.ImageField(upload_to='bundles', null=True)

    hook = models.CharField(max_length=255, null=True)
    description = RichTextField(null=True)

    discount = models.IntegerField(default=0)
    discount_price = models.DecimalField(max_digits=6, decimal_places=3, default=0)

    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def original_price(self):
        total = 0
        for course in self.courses.all():
            total += course.price
        return total

    def __str__(self):
        return self.name
    

class SaleMessage(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message + " - " + self.created_at.strftime("%d/%m/%Y %H:%M")