#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george
#
# Distributed under terms of the MIT license.
import urllib
import urllib2
import json
from datetime import datetime
from cStringIO import StringIO
import Image
import csv


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


def parse_img(url):
    API = "http://api.graymatics.com/grayit/process/image/ondemand"
    params = dict()
    params['API_KEY'] = "fa3ceb8a21ad6874e6e4d8cb127b8631"
    params['URL'] = url

    req = urllib2.Request(API, urllib.urlencode(params))
    raw = urllib2.urlopen(req).read()
    return raw


def img_database():
    keys = ['mayuki', 'audi', '溫布敦', '王建民', 'giant', '長靴']
    for key in keys:
        for img in google_search_image(key):
            yield key, img.get('url')


if __name__ == "__main__":
    result_file = open('/tmp/result.csv', 'w+')
    result_writer = csv.DictWriter(result_file, ['key', 'url', 'raw', 'delta_time'])

    error_file = open('/tmp/error.csv', 'w+')
    error_writer = csv.DictWriter(error_file, ['key', 'url', 'delta_time'])

    max_time = 0
    time_chain = []

    total = 0
    tmp = []
    for key, img in img_database():
        total += 1
        try:
            print img, key
            result = dict()
            result['key'] = key
            result['url'] = img
            last = datetime.now()
            result['raw'] = parse_img(img)
            delta_time = datetime.now() - last
            delta_time = delta_time.total_seconds()

            max_time = delta_time if delta_time > max_time else max_time
            result_writer.writerow(result)
            time_chain.append(delta_time)
            print result
        except Exception as e:
            print e
            delta_time = datetime.now() - last
            delta_time = delta_time.total_seconds()
            result['delta_time'] = delta_time
            error_writer.writerow(result)
            tmp.append((key, img))

    print 'second run'
    print tmp
    error = []
    for key, img in tmp:
        try:
            print img, key
            result['key'] = key
            result['url'] = img
            result = dict()
            last = datetime.now()
            result['raw'] = parse_img(img)
            delta_time = datetime.now() - last
            delta_time = delta_time.total_seconds()

            max_time = delta_time if delta_time > max_time else max_time
            result_writer.writerow(result)
            time_chain.append(delta_time)
            print result
        except:
            print e
            delta_time = datetime.now() - last
            delta_time = delta_time.total_seconds()
            result['delta_time'] = delta_time
            error_writer.writerow(result)
            error.append((key, img))

    worrying = len(tmp) - len(error)
    error = len(error)
    print '{} total, {} worrying, {} error'.format(total, worrying, error)
    avg_time = sum(time_chain) / len(time_chain)
    print 'max_time {}'.format(max_time)
    print 'avg_time {}'.format(avg_time)

    result_file.close()
