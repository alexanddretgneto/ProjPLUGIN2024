from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('noticias/<path:url>/', views.detalhes_noticia, name='detalhes_noticia'),  # alterei de 'link' para 'url'
]

