from django.shortcuts import render

def index(request):
    productos = [
        {"nombre": "Flan de vainilla",  "precio": 2500, "img": "web/img/flan_vainilla.jpeg"},
        {"nombre": "Flan de chocolate", "precio": 2800, "img": "web/img/flan_chocolate.jpeg"},
        {"nombre": "Flan vegano",       "precio": 3000, "img": "web/img/flan_vegano.jpeg"},
    ]
    return render(request, "web/index.html", {"productos": productos})

def about(request):
    datos = {
        "nombre_pyme": "OnlyFlans",
        "creacion": "2025-08-01",
        "descripcion": "Tienda de flanes artesanales con delivery.",
        "utilidad": "Descubrir, comparar y comprar flanes en línea.",
    }
    return render(request, "web/about.html", datos)

def welcome(request):
    nombre = request.GET.get("nombre")
    return render(request, "web/welcome.html", {"nombre": nombre})
