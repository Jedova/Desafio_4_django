from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def welcome(request):
    nombre = request.GET.get('nombre')
    return render(request, "welcome.html", {'nombre': nombre})