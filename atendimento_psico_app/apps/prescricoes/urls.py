from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'prescricoes'

router = routers.DefaultRouter()
router.register('', views.PrescricaoViewSet, basename='prescricoes')

urlpatterns = [
    path('', include(router.urls) )
]