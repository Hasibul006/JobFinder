from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'candidate'})
    file = models.FileField(upload_to='resumes/')
    text = models.TextField(blank=True, help_text="Extracted text from resume")
    skills = models.TextField(blank=True, help_text="Extracted skills as comma-separated list")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Resume"

class JobPost(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'recruiter'})
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_skills = models.TextField(help_text="Comma-separated skills")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Match(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    score = models.FloatField(help_text="Match score between 0 and 1")
    matched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Match: {self.resume.user.username} - {self.job.title} ({self.score:.2f})"

