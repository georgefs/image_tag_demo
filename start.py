#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george
#
# Distributed under terms of the MIT license.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

from Tag.models import Log, Image
import urllib
import urllib2
import datetime


def parse_img(url):
    API = "http://api.graymatics.com/grayit/process/image/ondemand"
    params = dict()
    params['API_KEY'] = "fa3ceb8a21ad6874e6e4d8cb127b8631"
    params['URL'] = url

    req = urllib2.Request(API, urllib.urlencode(params))
    raw = urllib2.urlopen(req).read()
    return raw


if __name__ == '__main__':
    for img in Image.objects.all():
        try:
            url = img.url
            last = datetime.datetime.now()
            result = parse_img(url)
            status = 1
        except:
            status = 0
        finally:
            delta_time = datetime.datetime.now() - last
            delta_seconds = delta_time.total_seconds()

            count = Log.objects.filter(image=img).count() + 1

            log = Log(
                image=img,
                status=status,
                result=locals().get('result'),
                delta_seconds=delta_seconds,
                count=count
            )
            log.save()
