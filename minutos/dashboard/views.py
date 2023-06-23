# 
# from python


from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta

# from django
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect

from project.models import Entry
from team.models import Team

# from utilities

from .utilities import get_time_for_user_and_date, get_time_for_team_and_month, time_for_user_and_month, get_time_for_user_and_project_and_month, get_time_for_user_and_team_month
# Create your views here.

@login_required
def dashboard(request):
    if not request.user.userprofile.active_team_id:
        redirect('my-account')

    team = get_object_or_404(Team, pk = request.user.userprofile.active_team_id, status = Team.ACTIVE)
    all_projects = team.projects.all()
    members = team.members.all()

    num_days = int(request.GET.get('num_days', 0))
    print(num_days)
    date_user = datetime.now() - timedelta(days=num_days)
    print(date_user)
    date_entries = Entry.objects.filter(team = team, created_at__date = date_user, created_by = request.user, is_tracked = True)

    context = {
        'team':team,
        'all_projects': all_projects,
        'members': members,
        'num_days': date_entries,
        'date_entries' : date_entries,
        'date_user':date_user,
        'get_time_for_user_and_date': get_time_for_user_and_date(team, request.user, date_user )
    }


    return render(request, 'dashboard/dashboard.html', context)