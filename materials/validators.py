import re
from rest_framework.serializers import ValidationError


def validate_forbidden_urls(value):
    url_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    urls = re.findall(url_pattern, value)

    if urls:
        for url in urls:
            if "youtube.com" not in url:
                raise ValidationError("Ссылки разрешены только на youtube.com.")
