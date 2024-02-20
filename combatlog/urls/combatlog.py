""" CombatLog URLs """

from combatlog import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register("combatlog", views.CombatLogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
