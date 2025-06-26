from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EspecialidadeViewSet, ProfissionalViewSet, ProfissionalEspecialidadeViewSet

router = DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'profissionais', ProfissionalViewSet)
router.register(r'profissional-especialidades', ProfissionalEspecialidadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
