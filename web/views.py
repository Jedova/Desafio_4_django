from django.shortcuts import render, redirect
from .forms import ContactFormForm
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
        form = ContactFormForm(request.POST)
        if form.is_valid():
            ContactForm.objects.create(
                customer_email=form.cleaned_data["customer_email"],
                customer_name=form.cleaned_data["customer_name"],
                message=form.cleaned_data["message"],
            )
            messages.success(request, "Gracias, recibimos tu mensaje.")
            return redirect("success")
    else:
        form = ContactFormForm()
    return render(request, "web/contact.html", {"form": form})

def success(request):
    return render(request, "web/success.html")