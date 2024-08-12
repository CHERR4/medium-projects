from datetime import UTC, datetime


def get_utc_datetime() -> datetime:
    return datetime.now(UTC)
