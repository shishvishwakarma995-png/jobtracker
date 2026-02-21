from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):

    # Status choices — stored as short codes, displayed as readable labels
    STATUS_CHOICES = [
        ('applied',      'Applied'),
        ('interviewing', 'Interviewing'),
        ('offer',        'Offer Received'),
        ('rejected',     'Rejected'),
        ('withdrawn',    'Withdrawn'),
    ]

    # Each job belongs to a user — if user is deleted, their jobs are deleted too
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    # Core fields
    company     = models.CharField(max_length=200)
    role        = models.CharField(max_length=200)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    location    = models.CharField(max_length=200, blank=True)  # optional
    job_url     = models.URLField(blank=True)                   # optional link to job posting

    # Dates
    applied_date    = models.DateField()
    interview_date  = models.DateField(null=True, blank=True)   # optional

    # Free text notes
    notes = models.TextField(blank=True)

    # Auto-tracked timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Show most recently applied jobs first by default
        ordering = ['-applied_date']

    def __str__(self):
        return f"{self.role} at {self.company} ({self.get_status_display()})"