from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')[:5]  
    return render(request, 'tasks/home.html', {'tasks': tasks})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'tasks/signup.html', {'form': form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('due_date', '-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
