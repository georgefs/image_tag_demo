#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george
#
# Distributed under terms of the MIT license.

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")


import urllib
import urllib2
from cStringIO import StringIO
import Image
import json
from Tag.models import Image as Tag_Image


#chick img_url is on live
def image_check(img_url):
    try:
        img = StringIO(urllib2.urlopen(img_url).read())
        Image.open(img)
        return True
    except:
        return False


#get google search image
def google_search_image(keyword):
    if not keyword:
        return

    api = "https://ajax.googleapis.com/ajax/services/search/images?"
    data = dict()
    data['v'] = '1.0'
    data['q'] = keyword
    data['imgsz'] = 'large'
    data['rsz'] = 8
    data['start'] = 0

    while True:
        data['start'] += data['rsz']
        url = api + urllib.urlencode(data)
        result = json.loads(urllib2.urlopen(url).read())

        if result.get('responseStatus') != 200:
            break

        img_infos = result.get('responseData', {}).get('results', [])
        for img_info in img_infos:

            if image_check(img_info.get('url')):
                yield img_info


if __name__ == "__main__":
    keys = ['mayuki', 'audi', '溫布敦', '王建民', 'giant', '長靴']
    for key in keys:
        for img in google_search_image(key):
            url = img.get('url')
            print url, key
            image = Tag_Image(url=url, key=key)
            image.save()
