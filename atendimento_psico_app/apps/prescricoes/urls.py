from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrescricaoViewSet, MedicamentoItemViewSet

router = DefaultRouter()
router.register(r'prescricoes', PrescricaoViewSet)
router.register(r'itens', MedicamentoItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
