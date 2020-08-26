from datetime import datetime, timezone


def format_timestamp(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp, timezone.utc).strftime('%H:%M:%S.%f')[:-3]
