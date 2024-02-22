from django.urls import path
from . import views

urlpatterns = [
    # path('', views.noticias, name='noticias'),
    # path('noticias/<path:url>/', views.detalhes_noticia, name='detalhes_noticia'),  # alterei de 'link' para 'url'
    
    path('', views.news_list, name='news_list'),
    path('details/<int:news_id>/', views.news_detail, name='news_detail'),
]

