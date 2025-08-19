from urllib.parse import urlparse

from rest_framework.serializers import ValidationError


valid_link = "https://www.youtube.com/"

def validate_youtube(value):
    if valid_link not in value:
        raise ValidationError("Недопустимая ссылка")