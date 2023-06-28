# from python
import json
from datetime import datetime, timezone

# from django
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# from models 

from team.models import Team
from .models import Entry

# api view

def  api_start_timer(request):
    
    entry = Entry.objects.create(
        minutes = 0 ,
        is_tracked = False,
        team_id = request.user.userprofile.ative_team_id,
        created_by = request.user,
        created_at = datetime.now()
    )

    return JsonResponse({'success':True,})


def api_stop_timer(request):
    entry = Entry.objects.get(
        minutes = 0 ,
        is_tracked = False,
        team_id = request.user.userprofile.ative_team_id,
        created_by = request.user,
    )

    tracked_minutes  = int(datetime.now(timezone.utc) - entry.created_at).total_seconds()/60

    if tracked_minutes <1 :
        tracked_minutes = 1
    
    entry.minutes = tracked_minutes
    entry.is_tracked = False
    entry.save()

    return JsonResponse({'success':True, 'entryID':entry.id})


def api_discard_timer(request):
    entries = Entry.objects.filter(team_id = request.user.userprofile.active_team_id, created_by = request.user, is_tracked = False)

    if entries:
        entry = entries.first()
        entry.delete()

    return JsonResponse({'success': True})