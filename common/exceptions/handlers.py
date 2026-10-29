"""
Global exception handler for HRMS APIs.
Returns a consistent error envelope: { status, message, errors }.
"""

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Custom DRF exception handler returning a consistent error contract.

    Response format:
    {
        "status": "error",
        "message": "Human-readable summary",
        "errors": { field: [messages] } | null
    }
    """
    response = exception_handler(exc, context)

    if response is not None:
        error_data = {
            'status': 'error',
            'message': _extract_message(response.data),
            'errors': _extract_errors(response.data),
        }
        response.data = error_data
    else:
        # Unhandled exception — return 500
        logger.exception("Unhandled exception: %s", exc)
        response = Response(
            {
                'status': 'error',
                'message': 'An unexpected error occurred. Please try again later.',
                'errors': None,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return response


def _extract_message(data):
    if isinstance(data, dict):
        if 'detail' in data:
            return str(data['detail'])
        return 'Validation failed. Please check the errors below.'
    if isinstance(data, list):
        return str(data[0]) if data else 'An error occurred.'
    return str(data)


def _extract_errors(data):
    if isinstance(data, dict) and 'detail' not in data:
        return data
    return None
