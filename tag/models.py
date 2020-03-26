from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _

from lib.basemodel import BaseModel


class Tag(BaseModel):
    name = models.CharField(verbose_name='name',unique=True, max_length=12)
    id = models.SmallIntegerField(primary_key=True, verbose_name='tag_id')

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
