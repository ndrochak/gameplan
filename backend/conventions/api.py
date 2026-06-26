import json
from typing import Any

from django.db import IntegrityError
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import CONVENTION_FIELDS, ConventionWriteForm
from .models import Convention

def serialize_convention(convention: Convention) -> dict[str, Any]:
    return {
        "id": convention.id,
        "name": convention.name,
        "start_date": convention.start_date.isoformat(),
        "end_date": convention.end_date.isoformat(),
        "location": convention.location,
        "timezone": convention.timezone,
        "daily_open_time": convention.daily_open_time.strftime("%H:%M:%S"),
        "daily_close_time": convention.daily_close_time.strftime("%H:%M:%S"),
        "maximum_attendance_capacity": convention.maximum_attendance_capacity,
        "created_at": convention.created_at.isoformat(),
        "updated_at": convention.updated_at.isoformat(),
    }


def parse_json_body(request: HttpRequest) -> tuple[dict[str, Any] | None, JsonResponse | None]:
    try:
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except UnicodeDecodeError:
        return None, error_response({"body": ["Request body must be valid UTF-8."]})
    except json.JSONDecodeError:
        return None, error_response({"body": ["Request body must be valid JSON."]})

    if not isinstance(payload, dict):
        return None, error_response({"body": ["Request body must be a JSON object."]})

    return payload, None


def error_response(errors: dict[str, list[str]], status: int = 400) -> JsonResponse:
    return JsonResponse({"errors": errors}, status=status)


def unknown_field_errors(payload: dict[str, Any]) -> dict[str, list[str]]:
    unknown_fields = sorted(set(payload) - set(CONVENTION_FIELDS))
    if unknown_fields:
        return {
            "non_field_errors": ["Unknown field(s): " + ", ".join(unknown_fields) + "."]
        }

    return {}


def form_errors_to_dict(form: ConventionWriteForm) -> dict[str, list[str]]:
    errors: dict[str, list[str]] = {}
    for field, messages in form.errors.get_json_data().items():
        key = "non_field_errors" if field == "__all__" else field
        errors[key] = [entry["message"] for entry in messages]
    return errors


def save_form(form: ConventionWriteForm) -> tuple[Convention | None, JsonResponse | None]:
    try:
        convention = form.save()
    except IntegrityError as exc:
        error_message = str(exc).lower()
        if any(name in error_message for name in {
            "convention_end_date_on_or_after_start_date",
            "convention_daily_close_after_open",
            "convention_capacity_positive",
        }):
            return None, error_response(
                {
                    "non_field_errors": [
                        "Convention data violates a database constraint."
                    ]
                },
                status=409,
            )
        raise

    return convention, None


@csrf_exempt
@require_http_methods(["GET", "POST"])
def convention_collection(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        conventions = Convention.objects.all()
        return JsonResponse({"conventions": [serialize_convention(c) for c in conventions]})

    payload, error = parse_json_body(request)
    if error:
        return error

    checked_payload = payload or {}

    errors = unknown_field_errors(checked_payload)
    if errors:
        return error_response(errors)

    form = ConventionWriteForm(data=checked_payload)
    if not form.is_valid():
        return error_response(form_errors_to_dict(form))

    convention, error = save_form(form)
    if error:
        return error

    return JsonResponse({"convention": serialize_convention(convention)}, status=201)


TIMEZONE_OPTIONS = [
    {"value": "UTC", "label": "UTC+0 UTC"},
    {"value": "Europe/London", "label": "UTC+0 Europe/London"},
    {"value": "Europe/Paris", "label": "UTC+1 Europe/Paris"},
    {"value": "Europe/Athens", "label": "UTC+2 Europe/Athens"},
    {"value": "Europe/Moscow", "label": "UTC+3 Europe/Moscow"},
    {"value": "Asia/Tehran", "label": "UTC+3:30 Asia/Tehran"},
    {"value": "Asia/Dubai", "label": "UTC+4 Asia/Dubai"},
    {"value": "Asia/Kabul", "label": "UTC+4:30 Asia/Kabul"},
    {"value": "Asia/Karachi", "label": "UTC+5 Asia/Karachi"},
    {"value": "Asia/Kolkata", "label": "UTC+5:30 Asia/Kolkata"},
    {"value": "Asia/Kathmandu", "label": "UTC+5:45 Asia/Kathmandu"},
    {"value": "Asia/Dhaka", "label": "UTC+6 Asia/Dhaka"},
    {"value": "Asia/Yangon", "label": "UTC+6:30 Asia/Yangon"},
    {"value": "Asia/Bangkok", "label": "UTC+7 Asia/Bangkok"},
    {"value": "Asia/Shanghai", "label": "UTC+8 Asia/Shanghai"},
    {"value": "Asia/Tokyo", "label": "UTC+9 Asia/Tokyo"},
    {"value": "Australia/Darwin", "label": "UTC+9:30 Australia/Darwin"},
    {"value": "Australia/Sydney", "label": "UTC+10 Australia/Sydney"},
    {"value": "Pacific/Noumea", "label": "UTC+11 Pacific/Noumea"},
    {"value": "Pacific/Auckland", "label": "UTC+12 Pacific/Auckland"},
    {"value": "Pacific/Pago_Pago", "label": "UTC-11 Pacific/Pago_Pago"},
    {"value": "Pacific/Honolulu", "label": "UTC-10 Pacific/Honolulu"},
    {"value": "America/Anchorage", "label": "UTC-9 America/Anchorage"},
    {"value": "America/Los_Angeles", "label": "UTC-8 America/Los_Angeles"},
    {"value": "America/Denver", "label": "UTC-7 America/Denver"},
    {"value": "America/Chicago", "label": "UTC-6 America/Chicago"},
    {"value": "America/New_York", "label": "UTC-5 America/New_York"},
    {"value": "America/Halifax", "label": "UTC-4 America/Halifax"},
    {"value": "America/Sao_Paulo", "label": "UTC-3 America/Sao_Paulo"},
    {"value": "Atlantic/Azores", "label": "UTC-1 Atlantic/Azores"},
]

@require_http_methods(["GET"])
def timezone_options(_request: HttpRequest) -> JsonResponse:
    return JsonResponse({"timezones": TIMEZONE_OPTIONS})


@csrf_exempt
@require_http_methods(["GET", "PUT", "PATCH"])
def convention_detail(request: HttpRequest, convention_id: int) -> JsonResponse:
    convention = get_object_or_404(Convention, id=convention_id)

    if request.method == "GET":
        return JsonResponse({"convention": serialize_convention(convention)})

    payload, error = parse_json_body(request)
    if error:
        return error

    checked_payload = payload or {}

    errors = unknown_field_errors(checked_payload)
    if errors:
        return error_response(errors)

    form = ConventionWriteForm(
        data=checked_payload,
        instance=convention,
        partial=request.method == "PATCH",
    )

    if not form.is_valid():
        return error_response(form_errors_to_dict(form))

    convention, error = save_form(form)
    if error:
        return error

    return JsonResponse({"convention": serialize_convention(convention)})
