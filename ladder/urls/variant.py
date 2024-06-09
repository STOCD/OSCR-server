""" Variant URLs """

from django.urls import include, path
from rest_framework import routers

from ladder import views

router = routers.DefaultRouter()
router.register("variant", views.VariantViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
