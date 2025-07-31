from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignalViewSet

router = DefaultRouter()
router.register(r'signals', SignalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
