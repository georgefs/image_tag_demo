#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george
#
# Distributed under terms of the MIT license.

from django.contrib import admin
from models import Image, Log

class LogAdmin(admin.ModelAdmin):
    list_display=['image', 'count']

admin.site.register(Image)
admin.site.register(Log, LogAdmin)
