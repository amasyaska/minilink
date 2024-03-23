from typing import Any
from django.db import models

def url_hash(url: str):
    return url


class URL(models.Model):
    def __init__(self, url: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.long_url = url
        self.short_url = url_hash(url)

    long_url = models.CharField(max_length=2084, unique=True)
    short_url = models.CharField(max_length=100)
    clicks = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.long_url} shortened to {self.short_url}'