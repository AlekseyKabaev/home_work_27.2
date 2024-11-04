import re

from rest_framework.exceptions import ValidationError


class YouTubeLinkValidator:
    def __call__(self, value):
        if not re.match(r'^https?://(www\.)?youtube\.com/', value):
            raise ValidationError('Ссылки на сторонние ресурсы, кроме youtube.com, запрещены.')
