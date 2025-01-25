# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Card(models.Model):

    #__Card_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    id = models.TextField(max_length=255, null=True, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    #__Card_FIELDS__END

    class Meta:
        verbose_name        = _("Card")
        verbose_name_plural = _("Card")


class Collection(models.Model):

    #__Collection_FIELDS__
    id = models.TextField(max_length=255, null=True, blank=True)

    #__Collection_FIELDS__END

    class Meta:
        verbose_name        = _("Collection")
        verbose_name_plural = _("Collection")



#__MODELS__END
