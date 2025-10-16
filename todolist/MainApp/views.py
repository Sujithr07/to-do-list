from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.contrib import messages

@login_required
def home(request):

    if request.method=='POST':
        task=request.POST.get('task')

        new_task = Todo(
            user = user,
            content = task
        )
        new_task.save()

        messages.success(request, 'New task saved successfully!')
        return redirect('home')

    user_tasks = Todo.objects.filter(user=request.user).order_by('-timestamp')

    finished_tasks = user_tasks.filter(is_completed=True).count()
    unfinished_tasks = user_tasks.filter(is_completed=False).count()

    context = {
        'tasks': user_tasks,
        'finished_tasks': finished_tasks,
        'unfinished_tasks': unfinished_tasks
    }

    return render(request,'homepage/index.html')
