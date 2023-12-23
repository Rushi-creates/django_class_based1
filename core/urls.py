# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import YourModelViewSet

router = DefaultRouter()
router.register(r'your-model', YourModelViewSet, basename='your-model')

urlpatterns = [
    path('api/', include(router.urls)),
]
