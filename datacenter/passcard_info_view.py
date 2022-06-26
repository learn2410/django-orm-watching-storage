from django.shortcuts import render

from datacenter.models import Passcard, Visit, is_visit_long, get_duration, format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard=passcard.id):
        duration = f'{format_duration(get_duration(visit.entered_at, visit.leaved_at))}'
        if not visit.leaved_at:
            duration = f'{duration} - not leaved'
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': is_visit_long(visit)
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
