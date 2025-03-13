from django.core.exceptions import ValidationError
from urllib.parse import urlparse


def validate_video_url(value):
    if not value:
        return
    parsed_url = urlparse(value)
    domain = parsed_url.netloc.lower()
    if domain and domain not in ['youtube.com', 'www.youtube.com']:
        raise ValidationError(
            "Ссылки на сторонние ресурсы, кроме youtube.com, запрещены."
        )
