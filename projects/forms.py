from django import forms
from django.utils.text import slugify
from .models import Task
from .models import Project
from register.models import Company
from django.contrib.auth.models import User


class TaskRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    # TODO: can explore that for assigning projects
    # assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    task_name = forms.CharField(max_length=80)
    reward = forms.FloatField()
    dead_line = forms.DateField()
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Task
        fields = [
            "project",
            "task_name",
            "reward",
            "dead_line",
            "description",
        ]


    def save(self, commit=True):
        task = super(TaskRegistrationForm, self).save(commit=False)
        task.project = self.cleaned_data['project']
        task.task_name = self.cleaned_data['task_name']
        task.reward = self.cleaned_data['reward']
        task.dead_line = self.cleaned_data['dead_line']
        task.description = self.cleaned_data['description']

        if commit:
            task.save()

        return task


    def __init__(self, *args, **kwargs):
        super(TaskRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Social Name'
        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['reward'].widget.attrs['class'] = 'form-control'
        self.fields['reward'].widget.attrs['placeholder'] = 'Token reward for the task'
        self.fields['dead_line'].widget.attrs['class'] = 'form-control'
        self.fields['dead_line'].widget.attrs['placeholder'] = 'Dead Line, type a date'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Type here the project description...'


class ProjectRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    owner = forms.CharField(max_length=80)
    efforts = forms.FloatField()
    dead_line = forms.DateField()

    # GILDS =(
    #     ("Education", "Education"),
    #     ("Developments", "Developments"),
    #     ("Governance", "Governance"),
    #     ("Legal", "Legal"),
    # )
    # Company is actually the GILDS
    # company = forms.ChoiceField(choices=GILDS)

    company = forms.CharField(max_length=80)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Project
        fields = [
            "name",
            "efforts",
            "dead_line",
            "owner",
            "description",
        ]


    def save(self, commit=True):
        Project = super(ProjectRegistrationForm, self).save(commit=False)
        Project.name = self.cleaned_data['name']
        Project.owner = self.cleaned_data['owner']
        Project.description = self.cleaned_data['description']
        Project.efforts = self.cleaned_data['efforts']
        Project.dead_line = self.cleaned_data['dead_line']
        Project.company = self.cleaned_data['company']
        Project.slug = slugify(str(self.cleaned_data['name']))

        if commit:
            Project.save()

        return Project


    def __init__(self, *args, **kwargs):
        super(ProjectRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Project Name'
        self.fields['owner'].widget.attrs['class'] = 'form-control'
        self.fields['owner'].widget.attrs['placeholder'] = 'Discord Username'
        self.fields['efforts'].widget.attrs['class'] = 'form-control'
        self.fields['efforts'].widget.attrs['placeholder'] = 'Bounty Reward'
        self.fields['dead_line'].widget.attrs['class'] = 'form-control'
        self.fields['dead_line'].widget.attrs['placeholder'] = 'Dead Line, type a date'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['placeholder'] = '---'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Type here the project description...'