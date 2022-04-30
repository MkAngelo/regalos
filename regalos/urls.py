"""regalos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconfs
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import regalos.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.InicioView.as_view(), name='inicio'),
    path('invitado/<int:id>/', views.InvitadoView.as_view(), name='invitado'),
    path('invitado/<int:event_id>/<str:event_type>/', views.compra_view, name='compra'),
    path('invitado/<int:event_id>/<str:event_type>/<int:regalo_id>/', views.pagar_view, name='pagar'),
    path('invitado/completado/', views.completado_view, name='completado'),
    path('anfitrion/', include(('anfitrion.urls', 'anfitrion'), namespace='anfitrion')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
