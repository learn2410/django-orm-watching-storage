from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit, get_duration, format_duration


def storage_information_view(request):
    queryset = Visit.objects.select_related('passcard').filter(leaved_at__isnull=True) \
        .values('passcard__owner_name', 'entered_at')
    non_closed_visits = []
    for visitor in queryset:
        non_closed_visits.append({
            'who_entered': visitor['passcard__owner_name'],
            'entered_at': localtime(visitor["entered_at"]),
            'duration': format_duration(get_duration(visitor["entered_at"]))
        })
    context = {'non_closed_visits': non_closed_visits}
    return render(request, 'storage_information.html', context)
