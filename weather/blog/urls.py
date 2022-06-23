from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *

router = DefaultRouter()
router.register('descriptions',weatherViewset)

urlpatterns = [
    path("",include(router.urls))
]