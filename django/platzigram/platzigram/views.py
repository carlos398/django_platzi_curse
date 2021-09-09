"""platzigram views"""

#django

from django import http
from django.http import HttpResponse
from django.http import JsonResponse

# utilities
from datetime import datetime
import json


def hello_world(request):
    return HttpResponse('Hola!, el tiempo actual es {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))
    
    
def hi(request):
    """Hi"""
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    return JsonResponse({ "numbers" : sorted(numbers)},json_dumps_params={'indent': 4})


def hi2(request):
    """segunda forma de hacer un json"""
    numers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'integers sorted succesfuly'
    }
    
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )