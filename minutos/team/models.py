from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Team(models.Model):
    ACTIVE = 'active'
    DELETED = 'deleted'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted')
    )

    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='created_team', on_delete=models.CASCADE) 
    members = models.ManyToManyField(User, related_name='teams')
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    