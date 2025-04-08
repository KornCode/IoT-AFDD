import json
from functools import wraps

from django.http import JsonResponse


def validate_json(required_fields=None):
    required_fields = required_fields or []

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            try:
                data = json.loads(request.body)
            except Exception:
                return JsonResponse({"error": "Invalid JSON"}, status=400)

            for field in required_fields:
                if field not in data:
                    return JsonResponse({"error": f"Missing required field: {field}"}, status=400)

            request.validated_data = data
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
