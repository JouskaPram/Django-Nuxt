from django.contrib import admin
from django.urls import path,include
from restapi.views import *
from restapi.models import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Product',ProductViewsets)
router.register('category',CategoryViewsets)

urlpatterns = [
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),
    
]
