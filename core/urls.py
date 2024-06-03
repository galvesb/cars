from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import PersonViewSet, CarViewSet, BuyCarViewSet

router = DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'cars', CarViewSet)
router.register(r'buycars', BuyCarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
