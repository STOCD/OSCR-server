""" CombatLog URLs """

from django.urls import include, path
from rest_framework import routers

from combatlog import views

router = routers.DefaultRouter()
router.register("combatlog", views.CombatLogViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "ui/combatlog/<int:pk>/",
        views.CombatLogDetailView.as_view(template_name="combatlog.html"),
        name="combatlog",
    ),
]
