from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'milk-metrics', views.MilkMetricViewSet)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/', include(router.urls)),
    path('api/esp32/', views.esp32_data, name='esp32_data'),
]
