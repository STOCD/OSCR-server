""" Custom Pagination """

from rest_framework.pagination import PageNumberPagination


class PageNumberPagination(PageNumberPagination):
    """
    Custom pagination class
    """

    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 1000


class AllResultsPagination(PageNumberPagination):
    """
    Custom pagination class
    """

    page_size = 10000
    page_size_query_param = "page_size"
    max_page_size = 10000
