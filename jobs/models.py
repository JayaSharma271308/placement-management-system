from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    website = models.URLField()
    package = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    salary = models.CharField(max_length=20)
    eligibility = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    skills = models.TextField(blank=True)
    cover_letter = models.TextField(blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
    max_length=20,
    default="Applied"
)

    def __str__(self):
        return f"{self.student.name} - {self.job.title}"
    
    