from django.utils.timezone import localtime,now


def get_duration(visit):
    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = now() - visit.entered_at
    return duration


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    hours = duration.seconds // SECONDS_IN_HOUR
    minutes = (duration.seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE

    formatted = f"{hours}ч {minutes}м"
    return formatted


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    SECONDS_IN_MINUTE = 60
    total_minutes = int(duration.total_seconds()// SECONDS_IN_MINUTE)
    return total_minutes>60
