# from python

from datetime import datetime, timezone

# from django

from django.shortcuts import get_object_or_404

# from models

from team.models import Team
from project.models import Entry



def active_entry(request):
    if request.user.is_authenticated:
        if request.user.userprofile.active_team_id:
            team = get_object_or_404(Team, pk = request.user.userprofile.active_team_id, status = Team.ACTIVE)
            unatract_entries = Entry.objects.filter(team = team, minutes = 0, created_by = request.user, is_tracked = False )

            if unatract_entries:
                active_entry = unatract_entries.first()
                active_entry.seconds_since = int((datetime.now(timezone.utc) - active_entry.created_at).total_seconds())

                return {'active_entry_seconds': active_entry.seconds_since, 'start_time':active_entry.created_at}
        
    return{'active_entry_seconds':0,'start_time': datetime.now().isoformat() }