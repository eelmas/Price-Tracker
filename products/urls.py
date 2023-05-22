from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

router = DefaultRouter()

router.register(r'my-models', ProductViewSet)
urlpatterns = [

]

urlpatterns += router.urls
