# Create your views here.
from django.shortcuts import render_to_response
from models import Log
import json


def line(request):
    logs = Log.objects.filter(count__lte=4)

    data = dict()
    for log in logs:
        img = log.image.url
        count = log.count
        container = data.get(img, [None, None, None, None])
        container[count - 1] = log.delta_seconds
        data[img] = container

    result = [['url', '1', '2', '3', '4']]
    for name, value in data.items():
        result.append([name] + value)

    result = json.dumps(result)
    print result

    return render_to_response('Tag/line.html', {'data':result})
