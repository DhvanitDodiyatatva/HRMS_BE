"""
Standard pagination classes for HRMS APIs.
"""

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    """
    Default pagination: 20 items per page, configurable via `page_size` query param.
    """
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'status': 'success',
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'status': {'type': 'string', 'example': 'success'},
                'count': {'type': 'integer', 'example': 100},
                'total_pages': {'type': 'integer', 'example': 5},
                'current_page': {'type': 'integer', 'example': 1},
                'next': {'type': 'string', 'nullable': True},
                'previous': {'type': 'string', 'nullable': True},
                'results': schema,
            },
        }


class LargeResultsSetPagination(PageNumberPagination):
    """For export-like endpoints needing larger page sizes."""
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 500
