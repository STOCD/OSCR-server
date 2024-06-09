""" Ladder Filter """

from core.filters import BaseFilterSet
from ladder.models import Ladder


class LadderFilter(BaseFilterSet):
    """Filter for model"""

    class Meta:
        """Meta class for filter"""

        model = Ladder
        exclude = [
            "internal_name",
            "internal_difficulty",
        ]
