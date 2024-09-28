"""LadderEntry Views"""

import logging

from django.core.exceptions import ImproperlyConfigured
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.urls import reverse
from django_filters.views import FilterView
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from core.filters import BaseFilterBackend
from core.pagination import PageNumberPagination
from ladder.filters import LadderEntryFilter
from ladder.models import LadderEntry, Variant
from ladder.serializers import LadderEntrySerializer

LOGGER = logging.getLogger("django")


class LadderEntryViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
):
    """LadderEntry API"""

    queryset = LadderEntry.objects.filter(visible=True)
    serializer_class = LadderEntrySerializer
    pagination_class = PageNumberPagination
    filter_backends = (BaseFilterBackend, OrderingFilter)
    filterset_class = LadderEntryFilter
    ordering_fields = [
        "player",
        "ladder",
        "ladder__name",
        "ladder__difficulty",
    ]
    ordering = "-data__DPS"

    def __init__(self, *args, **kwargs):
        """Bootstrap our filter"""
        LadderEntryFilter()
        self.ordering_fields = LadderEntry.ordering_fields()


class LadderEntryView(FilterView):
    """LadderEntry View"""

    model = LadderEntry
    filter_backends = (BaseFilterBackend, OrderingFilter)
    filterset_class = LadderEntryFilter
    ordering = "-data__DPS"
    paginate_by = 15

    def get_queryset(self):
        """Custom Queryset - Hide unverified results"""
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {"cls": self.__class__.__name__}
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset.filter(visible=True)

    def get(self, request, *args, **kwargs):
        """Override GET to add parameters into the request object."""
        if "search" not in request.GET:
            base_url = reverse("ladder_entries")
            query_string = request.GET.copy()
            query_string["search"] = "1"
            query_string["ladder__variant__name"] = (
                Variant.objects.exclude(name="Default")
                .order_by("-start_date")
                .first()
                .name
            )
            url = f"{base_url}?{query_string.urlencode()}"
            return HttpResponseRedirect(url)
        else:
            request.GET._mutable = True
            request.GET.pop("search")
            request.GET._mutable = False
        return super().get(request, *args, **kwargs)


class LadderInvitesView(FilterView):
    """LadderEntry View"""

    model = LadderEntry
    filter_backends = (BaseFilterBackend, OrderingFilter)
    filterset_class = LadderEntryFilter
    ordering = "-data__DPS"

    def get_queryset(self):
        return (
            LadderEntry.objects.filter(
                ladder__internal_name__in=[
                    "Infected Space",
                    "Hive Space",
                    "Bug Hunt",
                    "Nukara Prime: Transdimensional Tactics",
                ],
            )
            .exclude(ladder__difficulty="Any")
            .order_by("ladder__id")
            # .distinct("ladder__difficulty", "player")
        )

    def get_stream(self):
        """Return queryset as stream response."""
        yield "<pre>"
        for entry in self.get_queryset():
            for channel in entry.ladder_entry_channels():
                yield f"/channel_invite {channel} {entry.player}\n"
        yield "</pre>"

    def get(self, request, *args, **kwargs):
        """Overload for HTTP Get Method."""
        response = StreamingHttpResponse(self.get_stream())
        response["Cache-Control"] = "no-cache"
        response["X-Accel-Buffering"] = "no"
        return response
