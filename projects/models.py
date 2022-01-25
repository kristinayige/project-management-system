from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)

# Create your models here.
class Project(models.Model):
    declared = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    company = models.CharField(max_length=80)
    slug = models.SlugField('shortcut', blank=True)
    efforts = models.FloatField()
    status = models.CharField(max_length=7, choices=status, default=1)
    dead_line = models.DateField()
    owner = models.CharField(max_length=80, default="")
    # claimed = models.ManyToManyField(User)
    description = models.TextField(blank=True)

    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='task_in_projects')
    task_name = models.CharField(max_length=80)
    reward = models.FloatField()
    description = models.TextField(blank=True)
    dead_line = models.DateField()
    status = models.CharField(max_length=80)

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)