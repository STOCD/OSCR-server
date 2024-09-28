"""URL URLs"""

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "ui/stats/",
        TemplateView.as_view(template_name="stats.html"),
        name="stats",
    ),
]
