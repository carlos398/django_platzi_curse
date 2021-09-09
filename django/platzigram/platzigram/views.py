"""platzigram views"""

#django
from django.http import HttpResponse
from django.http import JsonResponse

# utilities
from datetime import datetime



def hello_world(request):
    return HttpResponse('Hola!, el tiempo actual es {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))
    
    
def hi(request):
    """Hi"""
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    return JsonResponse({ "numbers" : sorted(numbers)},json_dumps_params={'indent': 4})