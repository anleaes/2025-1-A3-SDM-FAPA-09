from django.urls import path, include
from .views import CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls) )
]
