from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from lib.basemodel import BaseModel

User = get_user_model()


class Avatar(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile = models.ImageField(verbose_name='profile', upload_to='avatar/user/')

    class Meta:
        verbose_name = _('avatar')
        verbose_name_plural = _('avatars')