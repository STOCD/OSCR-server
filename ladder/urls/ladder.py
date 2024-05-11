""" Ladder URLs """

from django.urls import include, path
from rest_framework import routers

from ladder import views

router = routers.DefaultRouter()
router.register("ladder", views.LadderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
