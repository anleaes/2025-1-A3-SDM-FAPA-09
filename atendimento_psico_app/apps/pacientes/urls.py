from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pacientes'

router = routers.DefaultRouter()
router.register('', views.PacienteViewSet, basename='pacientes')

urlpatterns = [
    path('', include(router.urls) )
]