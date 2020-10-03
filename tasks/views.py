from django.shortcuts import render, redirect

from .models import *
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method =="POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}

    return render(request, 'content.html', context)

def done(request, pk):
    task = Task.objects.get(id=pk)

    if task.complete == True:
        task.complete = False
    else:
        task.complete = True
    
    task.save()

    return redirect('/')

def delete(request, pk):
    task = Task.objects.get(id=pk)

    task.delete()

    return redirect('/')
