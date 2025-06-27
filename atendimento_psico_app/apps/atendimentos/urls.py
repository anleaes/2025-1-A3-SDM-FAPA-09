from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'atendimentos'

router = routers.DefaultRouter()
router.register('', views.AtendimentoViewSet, basename='atendimentos')

urlpatterns = [
    path('', include(router.urls) )
]