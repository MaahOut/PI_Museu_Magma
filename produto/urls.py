from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('adicionar-estoque/<str:nome>/', views.adicionar_estoque, name='adicionar_estoque'),
    path('registrar-venda/<str:nome>/', views.registrar_venda, name='registrar_venda'),
    path('ajustar-estoque/<str:nome>/', views.ajustar_estoque, name='ajustar_estoque'),
    path('alterar-preco/<str:nome>/', views.alterar_preco, name='alterar_preco'),
    path('historico/<str:nome>/', views.ver_historico, name='ver_historico'),
]