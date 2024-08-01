from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to home page</h1>')

    #return render(request, 'home.html') 
    return render(request, 'home.html',{'name':'Miguel Alejandro Gomez Duque'})



def about(request):
    #return HttpResponse('<h2> Estoy usando el about</h2>')
    return render(request, 'about.html')
