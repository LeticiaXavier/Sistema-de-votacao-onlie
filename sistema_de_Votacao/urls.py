# sistema_de_votacao/urls.py

from django.contrib import admin
from django.urls import path, include  # Verifique se 'include' está aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('votacao/', include('votacao.urls')), # Verifique esta linha
]