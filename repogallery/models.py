#!/usr/bin/env python
# -*- coding: utf-8 -*-

# "THE WISKEY-WARE LICENSE":
# Juan BC <jbc.develop@gmail.com>
# wrote this file. As long as you retain this notice you can do whatever you
# want with this stuff. If we meet some day, and you think this stuff is worth
# it, you can buy me a WISKEY in return Juan BC


# =============================================================================
# IMPORTS
# =============================================================================

import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


# =============================================================================
# MODELS
# =============================================================================

def render_upload_resolver(gallery, filename):
    filename = "{}.html".format(gallery.uuid)
    return u"/".join(["gallery_renders", str(gallery.user.pk), filename])


class Gallery(models.Model):

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")

    active = models.BooleanField(default=True, verbose_name=_("Active"))

    user = models.ForeignKey(auth.get_user_model(), verbose_name=_("User"))
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name=_("UUID"))

    repository = models.URLField(verbose_name=_("Repository"))
    repository_folder = models.CharField(
        null=True, verbose_name=_("Repository Folder"))

    created_at = models.DatetimeField(
        auto_now_add=True, verbose_name=_("Created At"))
    last_build = models.DatetimeField(null=True, verbose_name=_("Last Build"))

    template = models.CharField(
        max_lenght=255, choices=TEMPLATES, verbose_name=_("Template"))
    render = models.FileField(
        null=True, upload_to=render_upload_resolver, verbose_name=_("Render"))

    def __unicode__(self):
        return "{} - {}".format(self.user, self.repository)






