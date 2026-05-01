from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={'title':'Главная страница',
             'content':'Home',
             'list':['first','second'],
             'bool':True }
    return render(request, 'main/index.html',context)

def about(request):
    return HttpResponse("About page.")
