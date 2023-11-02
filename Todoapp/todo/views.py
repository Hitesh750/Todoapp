from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Todo

# Create your views here.
def viewtask(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        data=Todo(name=nm)
        data.save()

    tasks=Todo.objects.all()
    context={'tasks':tasks}
    return render(request,'index.html',context)

def update_task(request,id):
    task = Todo.objects.get(id=id)
    if request.method=='POST':
        task.name=request.POST.get('name')
        task.save()
        messages.success(request, 'Updated Successfully')
        return redirect('/')
    else:
        return render(request, 'update_task.html',{'task':task})

def delete_task(request,id):
   task = Todo.objects.get(id=id)
   task.delete()
   return redirect('/')



