from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from category.models import Category
from lib.basemodel import BaseModel
from tag.models import Tag


class Post(BaseModel):
    title = models.CharField(max_length=20, verbose_name=_('title'),)
    body = models.TextField(verbose_name='body', blank=True)
    tag = models.ManyToManyField(Tag, related_name=_('tag'), blank=True)
    category = models.ManyToManyField(Category, related_name=_('category'),)
    # media = models.ImageField(verbose_name=_('media'))

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
