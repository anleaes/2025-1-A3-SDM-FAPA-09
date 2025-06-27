from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categories'

router = routers.DefaultRouter()
router.register('', views.CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls) )
]