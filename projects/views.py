from django.shortcuts import render
from django.db.models import Avg
from register.models import Project
from projects.models import Task
from projects.forms import TaskRegistrationForm
from projects.forms import ProjectRegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def projects(request):
    print("HERE")
    print(request.POST.get('task_id'))
    print(request.is_ajax())
    if request.method == 'POST':
        print("POST")
        print(request.is_ajax())
        task_id = request.POST.get('task_id')
        myUser = User.objects.get(pk=request.user.id)
        myTask = Task.objects.get(pk = task_id)
        myTask.claimed.add(myUser) #add the user to the task
        return JsonResponse({'status': 'ok'})
    projects = Project.objects.all()
    tasks = Task.objects.all()
    open_tasks = tasks.filter(status='Created')
    my_tasks = tasks.filter(claimed__in = [request.user.id]).values_list('id', flat = True)
    proj_dict = {}
    context = {
        'projects' : projects,
        'tasks' : tasks,
        'open_tasks' : open_tasks,
        'my_tasks': my_tasks,
    }
    print(my_tasks)
    return render(request, 'projects/projects.html', context)

def newTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            instance = form.save(commit = False)
            instance.status = "Created"
            instance.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_task.html', context)
        else:
            return render(request, 'projects/new_task.html', context)
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_task.html', context)

def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            instance = form.save(commit = False)
            instance.declared = User.objects.get(pk=request.user.id)
            instance.status = "Created"
            instance.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_project.html', context)
        else:
            print("bad here")
            return render(request, 'projects/new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_project.html', context)