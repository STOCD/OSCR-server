""" Variant Filter """

from core.filters import BaseFilterSet
from ladder.models import Variant


class VariantFilter(BaseFilterSet):
    """Filter for model"""

    class Meta:
        """Meta class for filter"""

        model = Variant
        exclude = []
