from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def cycle_status(self):
        next_status = {
            'pending': 'progress',
            'progress': 'completed',
            'completed': 'pending'
        }
        self.status = next_status[self.status]
        self.save()

    def __str__(self):
        return self.title
