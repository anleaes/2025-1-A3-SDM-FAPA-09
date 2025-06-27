from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'profissionais'

router = routers.DefaultRouter()
router.register('', views.EspecialidadeViewSet, basename='especialidade'),
router.register('', views.ProfissionalViewSet, basename='profissionais'),
router.register('', views.ProfissionalEspecialidadeViewSet, basename='profissionalespecialidade'),


urlpatterns = [
    path('', include(router.urls)),
]
