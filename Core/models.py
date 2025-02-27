from django.db import models

class Student(models.Model):
    BRANCH_CHOICES = [
        ('CS', 'Computer Science'),
        ('EC', 'Electronics and Communication'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering')
    ]
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES, default='CS')
    register_num = models.CharField(max_length=10, unique=True)