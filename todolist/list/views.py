from .models import *

from django.shortcuts import render

from .forms import TaskForm


def index(request):
    tasks = Tasks.objects.order_by("create_date")
    form = TaskForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'main.html', {"tasks": tasks, "form": form})
