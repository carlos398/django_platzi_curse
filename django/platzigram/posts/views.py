"""post views"""

#django
from django.shortcuts import render

#utilities
from datetime import datetime

# Create your views here.

posts = [
    {
        'title':'Mont Blanc',
        'user': {
            'name': 'Yesica Cortes',
            'picture': ''
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo' : ''
    }
]


def list_posts(request):
    """List existing posts"""
    return render(request, 'feed.html', {'posts': posts})