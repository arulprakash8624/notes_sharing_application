from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Student(AbstractUser):
    register_number = models.CharField(max_length=20, unique=True, verbose_name="Register Number")
    year = models.CharField(max_length=20, verbose_name="Year")
    dept = models.CharField(max_length=100, verbose_name="Department")
    section = models.CharField(max_length=10, verbose_name="Section")
    username = models.CharField(max_length=150, unique=True, verbose_name="Username")
    first_name = models.CharField(max_length=150, blank=True, verbose_name="First Name")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email")
    
    # Add unique related_name attributes
    groups = models.ManyToManyField(Group, related_name='student_users')
    user_permissions = models.ManyToManyField(Permission, related_name='student_users')

    def __str__(self):
        return self.username

class Staff(AbstractUser):
    staff_id = models.CharField(max_length=20, unique=True, verbose_name="Staff ID")
    position = models.CharField(max_length=100, verbose_name="Position")
    
    username = models.CharField(max_length=150, unique=True, verbose_name="Username")
    first_name = models.CharField(max_length=150, blank=True, verbose_name="First Name")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email")
    
    # Add unique related_name attributes
    groups = models.ManyToManyField(Group, related_name='staff_users')
    user_permissions = models.ManyToManyField(Permission, related_name='staff_users')

    def __str__(self):
        return self.username
class files(models.Model):
    name = models.CharField(max_length=150)
    files= models.FileField(max_length=100)
    staff_id=models.CharField(max_length=10)
    def __str__(self):
        return self.name