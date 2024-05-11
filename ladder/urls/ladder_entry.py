""" LadderEntry URLs """

from django.urls import include, path
from rest_framework import routers

from ladder import views

router = routers.DefaultRouter()
router.register("ladder-entries", views.LadderEntryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "ui/ladder-entries/",
        views.LadderEntryView.as_view(template_name="ladder_entry.html"),
        name="ladder_entries",
    ),
    path(
        "ui/",
        views.LadderEntryView.as_view(template_name="ladder_entry.html"),
    ),
]
