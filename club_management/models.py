import os
import django
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Patron', 'Patron'),
        ('Student', 'Student'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Student')

    def __str__(self):
        return f"{self.username} - {self.role}"

# Ensure Django settings are configured
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'victory_club.settings')

# Student Model
class Student(models.Model):
    admission_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=5)  # e.g., 2E, 3N, etc.

    def __str__(self):
        return f"{self.name} ({self.admission_number})"

# Club Model
class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    registration_fee = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name

# Patron Model (Teacher assigned to a club)
class Patron(models.Model):
    name = models.CharField(max_length=100)
    club = models.OneToOneField(Club, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - Patron of {self.club.name}"

# Membership Model
class Membership(models.Model):
    ROLE_CHOICES = [
        ('General', 'General Member'),
        ('Leader', 'Executive Leader')
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    join_date = models.DateField(auto_now_add=True)
    exit_date = models.DateField(null=True, blank=True)  # To track when a student leaves
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='General')
    
    def __str__(self):
        return f"{self.student.name} - {self.club.name} ({self.role})"

# Activity Model (For Club Events)
class Activity(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    occurrence_date = models.DateField()
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Optional
    
    def __str__(self):
        return f"{self.name} - {self.club.name}"

# Finance Model (Tracking Revenue and Allocations)
class Finance(models.Model):
    club = models.OneToOneField(Club, on_delete=models.CASCADE)
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    ongoing_activities_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    annual_parties_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    savings = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"Finance Record for {self.club.name}"
