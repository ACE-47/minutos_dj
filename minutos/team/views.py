# from python 

import random

# from django
# 
# 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect ,get_object_or_404

# from models
from .models import Team, Invitation


# from utilites
from .utilities import send_invitaion, send_invitaion_accepted

# Create your views here.


## make sure to modify the coede like (is_valid())

@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, pk = team_id, members__in = [request.user], status = Team.ACTIVE )
    invitations = team.invitations.filter( status = Invitation.INVITED)
    return render(request, 'team/team_detail.html', {
        'team':team,
        'invitations':invitations
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
    

def invite(request):
    team = get_object_or_404(Team, pk = request.user.userprofile.active_team_id, status = Team.ACTIVE)

    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            invitaions = Invitation.objects.filter(team = team, email = email)
            
            if not invitaions:
                code = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz123456789') for i in range(4))

                Invitation.objects.create(team = team, email= email, code = code)

                messages.info(request, 'The user was invited')
                send_invitaion(email, code, team)
                return redirect('team-detail',team_id =  team.id)
            else:
                messages.info(request, ' the user has already been invited')

    return render(request, 'team/invite.html',{'team':team})



