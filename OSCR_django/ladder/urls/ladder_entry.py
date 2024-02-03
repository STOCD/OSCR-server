""" LadderEntry URLs """

from django.urls import include, path
from ladder import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("ladder-entries", views.LadderEntryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
