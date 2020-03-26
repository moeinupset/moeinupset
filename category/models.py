from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from lib.basemodel import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=16, verbose_name=_('category'),)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categorys')
