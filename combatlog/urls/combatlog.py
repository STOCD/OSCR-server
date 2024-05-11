""" CombatLog URLs """

from django.urls import include, path
from rest_framework import routers

from combatlog import views

router = routers.DefaultRouter()
router.register("combatlog", views.CombatLogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
