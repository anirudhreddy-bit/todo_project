from django.shortcuts import render,redirect
from . models import TaskList

# Create your views here.
def index(request):
    lists =TaskList.objects.all()
    return render(request,'trello_app/index.html',{'lists':lists})

def create_list(request):
    if request.method == 'POST':
        list_name = request.POST['list_name']
        list = TaskList(name = list_name)
        list.save()
        return redirect('index')
    else:
        return render(request,'trello_app/new_list.html')