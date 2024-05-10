""" URL URLs """

from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("ui/", TemplateView.as_view(template_name="ui.html")),
]
