from django.shortcuts import render

def index(request):
    return render(request, 'pedido/index.html')  # Aponte para 'pedido/index.html'
