from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from category.models import Category
from lib.basemodel import BaseModel


class SubCategory(BaseModel):
    name = models.CharField(max_length=12, verbose_name=_('name'),)
    category = models.ManyToManyField(Category, related_name='sub_category')

    class Meta:
        verbose_name = _('sub_category')
        verbose_name_plural = _('sub_categorys')
