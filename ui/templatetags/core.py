"""Core Template Tags"""

import logging

from django import template

register = template.Library()
LOGGER = logging.getLogger("django")


@register.filter
def get(mapping, key):
    """Get from Dictionary"""
    return mapping.get(key)


@register.filter
def percentage(value):
    """Format as a percentage"""
    return float(value) * 100
