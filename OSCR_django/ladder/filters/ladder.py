""" Ladder Filter """

from core.filters import BaseFilterSet
from ladder.models import Ladder


class LadderFilter(BaseFilterSet):
    """Filter for Tasks API"""

    class Meta:
        """Meta class for the application filter"""

        model = Ladder
        exclude = [
            "internal_name",
            "internal_difficulty",
        ]
