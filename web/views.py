from django.shortcuts import render, redirect
from .forms import ContactFormModelForm
from .models import ContactForm, Flan
from django.contrib import messages

def index(request):
    
    flanes_publicos = Flan.objects.filter(is_private=False).order_by("name")
    return render(request, "web/index.html", {"flanes": flanes_publicos})

def about(request):
    datos = {
        "nombre_pyme": "OnlyFlans",
        "creacion": "2025-08-01",
        "descripcion": "Tienda de flanes artesanales con delivery.",
        "utilidad": "Descubrir, comparar y comprar flanes en línea.",
    }
    return render(request, "web/about.html", datos)

def welcome(request):
    
    flanes_privados = Flan.objects.filter(is_private=True).order_by("name")
    nombre = request.GET.get("nombre")
    return render(request, "web/welcome.html", {"nombre": nombre, "flanes": flanes_privados})

def contact(request):
    if request.method == "POST":
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("success")
    else:
        form = ContactFormModelForm()
    return render(request, "web/contact.html", {"form": form})

def success(request):
    return render(request, "web/success.html")

def catalogo(request):
    pub = Flan.objects.filter(is_private=False).order_by("name")
    priv = Flan.objects.filter(is_private=True).order_by("name")
    return render(request, "web/catalogo.html", {
        "publicos": pub, "privados": priv,
        "total_publicos": pub.count(), "total_privados": priv.count()
    })

from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False).order_by("name")
    return render(request, "web/index.html", {"flanes": flanes_publicos})

@ensure_csrf_cookie
def about(request):
    return render(request, "web/about.html", {
        "nombre_pyme": "OnlyFlans",
        "creacion": "2025-08-01",
        "descripcion": "Tienda de flanes artesanales con delivery.",
        "utilidad": "Descubrir, comparar y comprar flanes en línea.",
    })