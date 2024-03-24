from django.db import models
from .link_relay import convert_decimal_to_tetrasexagesimal


class CustomModelManager(models.Manager):
    def create(self, **data):
        """custom create method to convert long url to short url
        and write short url as URL model field"""
        data['short'] = convert_decimal_to_tetrasexagesimal(data['url'])
        return super().create(**data)


class PopularLinksManager(models.Manager):
    """Manager to get 10 most clickable urls"""
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().exclude(visits=0).order_by('-visits')[:10]


class URL(models.Model):
    url = models.CharField(max_length=2084, unique=True)
    short = models.CharField(max_length=100)
    visits = models.IntegerField(default=0)

    objects = CustomModelManager()
    popular = PopularLinksManager()

    def __str__(self) -> str:
        return f'{self.url} shortened to {self.short}'
    
    class Meta:
        ordering = ('-visits',)