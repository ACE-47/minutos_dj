from django.contrib.auth.models import User
from django.db import models


from team.models import Team
# Create your models here.

class Project(models.Model):
    team = models.ForeignKey(Team, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
    def registerd_time(self):
        return sum(entry.minutes for entry in self.entries.all())

    def num_tasks_todo(self):
        return self.tasks.filter(status = Task.TODO).count()
    
class Task(models.Model):

    TODO = 'todo'
    DONE = 'done'
    ARCHIVE ='archive'

    CHOICES_STATUS = (
    (ARCHIVE,'aRCHIVE'),
    (DONE,'Done'),
    (TODO, 'Todo')
    )

    team = models.ForeignKey(Team, related_name='tasks', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=TODO)

    class Meta:
        ordering = ['-created_by']

    def __str__(self):
        return self.title
    
    def registerd_time(self):
        return sum(entry.minutes for entry in self.entries.all())
    

class Entry(models.Model):
    team = models.ForeignKey(Team, related_name='entries', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='entries', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='entries', on_delete=models.CASCADE)
    minutes = models.IntegerField(default=0)
    is_tracked = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    class Meta:
        ordering = ['-created_by']

    def __str__(self):
        if self.task:
            return '%s - %s' % (self.task.title, self.created_by)
        
        return '%' % self.created_at
