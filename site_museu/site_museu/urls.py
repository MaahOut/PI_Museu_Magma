from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedido/', include('pedido.urls')),  # Redireciona para as urls da app pedido
    path('polls/', include('polls.urls')),    # Redireciona para as urls da app polls
    path('produto/', include('produto.urls')),  # Redireciona para as urls da app produto
    path('', include('produto.urls')),  # Se você quiser que a página inicial seja a index da app produto
    path('usuario/', include('usuario.urls')),  # Redireciona para as urls da app usuario
]
