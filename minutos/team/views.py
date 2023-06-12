
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect ,get_object_or_404

from .models import Team
# Create your views here.


## make sure to modify the coede like (is_valid())

@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, pk = team_id, members__in = [request.user], status = Team.ACTIVE )
    return render(request, 'team/team_detail.html', {
        'team':team
    })

@login_required
def activate_team(request, team_id):
    team = get_object_or_404(Team, pk = team_id, members__in = [request.user], status = Team.ACTIVE )
    userprofile = request.user.userprofile
    userprofile.active_team_id = team.id
    userprofile.save()

    messages.info(request, 'the tteam was activated')
    return redirect('team-detail', team.id) #shortcut that no need to wrrite it like this (team_id = team.id) since you have one argument

@login_required
def add_team(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            team = Team.objects.create(title = title, created_by = request.user)
            team.members.add(request.user)
            team.save()

            userprofile = request.user.userprofile
            userprofile.active_team_id = team.id
            userprofile.save()

            return redirect('my-account')
    else:
        return render(request, 'team/add_team.html')
    
@login_required
def edit_team(request):
    team = get_object_or_404(Team, pk = request.user.userprofile.active_team_id, members__in = [request.user], status = Team.ACTIVE )

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            team.title = title
            team.save()
            messages.info(request, 'the changes was successfuly saced')
            return redirect('team-detail',team_id = team.id)
    else:
        return render(request, 'team/edit_team.html',{
            'team':team,
        })
    