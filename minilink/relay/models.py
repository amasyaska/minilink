from typing import Any, Iterable
from django.db import models

def url_hash(url: str):
    return url


class PopularLinksManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().order_by('clicks')[:10]


class URL(models.Model):
    long_url = models.CharField(max_length=2084, unique=True)
    short_url = models.CharField(max_length=100)
    clicks = models.IntegerField(default=0)

    objects = models.Manager()
    popular = PopularLinksManager()

    def save(self, *args, **kwargs) -> None:
        self.short_url = url_hash(self.long_url)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.long_url} shortened to {self.short_url}'
    
    class Meta:
        ordering = ('clicks',)