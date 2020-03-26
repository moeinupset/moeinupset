from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from avatar.models import Avatar
from lib.basemodel import BaseModel

User = get_user_model()


class Author(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='author')
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, related_name='author_avatar', blank=True)

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
