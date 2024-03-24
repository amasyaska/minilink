from django.db import models

def url_hash(url: str):
    from random import randint
    return randint(1, 999_999)


class CustomModelManager(models.Manager):
    def create(self, **data):
        data['short_url'] = url_hash(data['long_url'])
        return super().create(**data)


class PopularLinksManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().exclude(clicks=0).order_by('-clicks')[:10]


class URL(models.Model):
    long_url = models.CharField(max_length=2084, unique=True)
    short_url = models.CharField(max_length=100)
    clicks = models.IntegerField(default=0)

    objects = CustomModelManager()
    popular = PopularLinksManager()

    def __str__(self) -> str:
        return f'{self.long_url} shortened to {self.short_url}'
    
    class Meta:
        ordering = ('clicks',)