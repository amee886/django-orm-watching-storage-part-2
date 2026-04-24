from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    published_posts=Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': published_posts, 
    }
    return render(request, 'active_passcards.html', context)
