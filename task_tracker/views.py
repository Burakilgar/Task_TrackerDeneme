from django.shortcuts import render,redirect
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task

from .serializer import TaskSerializer
from pprint import pprint
from .forms import StudentForm

from django.contrib import messages
from django.shortcuts import get_object_or_404,render
# Create your views here.


def home(request):
    return HttpResponse("Task Tracker")
@api_view()
def home2(request):
    
    return Response(
        {
          "message" : "task tracker"
        }
    )
    


def index(request):
    
    task=Task.objects.all()   
    # serializer = TaskSerializer(task, many=True)
    
    
    
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
       
        if form.is_valid():
            form.save()
           

   
    context={
        # "task" :serializer.data,
        "task" : task,
       'form': form
        }
    return render(request,"task_tracker/home.html" ,context)
    
    
    
   
def delete_task(request,pk):

    task=get_object_or_404(Task,id=pk)
    task.delete()
    messages.success(request, "City deleted")
    return redirect("index")
    
    
  
    