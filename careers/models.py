from django.db import models
from django.utils import timezone
from django.conf import settings

class JobApplication(models.Model):
    """Model to store job applications"""
    EXPERIENCE_CHOICES = [
        ('1-2', '1-2 years'),
        ('3-5', '3-5 years'),
        ('5+', '5+ years'),
    ]
    
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('interview', 'Interview Stage'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications', null=True)
    position = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
    resume = models.FileField(upload_to='resumes/')
    portfolio = models.URLField(blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    applied_on = models.DateTimeField(auto_now_add=True)
    applied_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    last_updated = models.DateTimeField(auto_now=True)
    admin_notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.position}"
    
    class Meta:
        ordering = ['-applied_at']