from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'medicamentos'

router = routers.DefaultRouter()
router.register('', views.MedicamentoViewSet, basename='medicamentos')

urlpatterns = [
    path('', include(router.urls) )
]