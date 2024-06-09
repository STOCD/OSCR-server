"""
URL configuration for OSCR_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view

from .openapi import openapi_info

schema_view = get_schema_view(
    openapi_info,
    public=True,
    permission_classes=(),
)


urlpatterns = [
    # path("", include("user.urls")),
    path("", include("combatlog.urls.combatlog")),
    path("", include("ladder.urls.ladder")),
    path("", include("ladder.urls.ladder_entry")),
    path("", include("ladder.urls.variant")),
    path("", include("ui.urls.ui")),
]

if settings.ADMIN_PATH:
    urlpatterns.append(path(settings.ADMIN_PATH, admin.site.urls))

if settings.SWAGGER_PATH:
    urlpatterns.append(path(settings.SWAGGER_PATH, schema_view.with_ui("swagger")))
