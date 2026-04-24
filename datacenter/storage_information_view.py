from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime,now
from datacenter.models import format_duration
from datacenter.models import get_duration 


def storage_information_view(request):
    visits = Visit.objects.select_related('passcard').filter(leaved_at__isnull=True)
    result = []
    for visit in visits:
        duration = get_duration(visit)
        result.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(duration),
        })

    context = {
        'non_closed_visits': result
    }
    return render(request, 'storage_information.html', context)

