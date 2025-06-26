"""
URL configuration for atendimento_psico_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/', include('apps.categories.urls')),
    path('api/profissionais/', include('apps.profissionais.urls')),
    path('api/pacientes/', include('apps.pacientes.urls')),
    path('api/atendimentos/', include('apps.atendimentos.urls')),
    path('api/medicamentos/', include('apps.medicamentos.urls')),
    path('api/prescricoes/', include('apps.prescricoes.urls')),
]

# declarar a pasta caminho e raiz para arquivos que sera enviados atraves de forms de upload.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
