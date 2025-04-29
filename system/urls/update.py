"""Update URLs"""

from django.urls import include, path
from rest_framework import routers

from system import views

router = routers.DefaultRouter()
router.register("system", views.UpdateViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
