from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request, plantilla="acerca.html"):
    return render(request,plantilla)
def productos(request):
    return render(request,'productos.html',{
        'mensaje':'Producto de Farmacia',
        'titulo':'medicamentos',
        'medicamentos':[{'descripcion':'paracetamol','precio':0.5,'stock': True},
                        {'descripcion': 'azitromicina', 'precio': 0.9, 'stock': True},
                        {'descripcion': 'buprex', 'precio': 0.65, 'stock': False},
                        {'descripcion': 'garamicina', 'precio': 0.65, 'stock': False},
                        {'descripcion': 'fisiol', 'precio': 0.65, 'stock': True}
                        ]
                      })
def descripcion(request):
    return render(request,'descripcion.html')