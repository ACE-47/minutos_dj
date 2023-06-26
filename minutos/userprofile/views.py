from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Userprofile

from team.models import Invitation

# from utilities 
from team.utilities import send_invitaion_accepted


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            userprofile = Userprofile.objects.create(user = user)
            login(request,user)

            invitations = Invitation.objects.filter(email = user.email, status = Invitation.INVITED)

            if invitations:
                return redirect('team-accept-invitaion')
            else:

                return redirect('dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'userprofile/signup.html',{
        'form':form
    })

@login_required
def myaccount(request):
    teams = request.user.teams.exclude(pk = request.user.userprofile.active_team_id)
    return render(request,'userprofile/myaccount.html',{
        'teams':teams
    })


@login_required
def edit_profile(request):

    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name','')
        request.user.last_name = request.POST.get('last_name','')
        request.user.email = request.POST.get('email','')
        request.user.save()

        messages.info(request,'the changes was saved')
        
        return redirect('my-account')
    
    else:
        return render(request, 'userprofile/edit_profile.html')
    

@login_required
def accept_invitation(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        invitaions =  Invitation.objects.filter(code = code, email = request.user.email)

        if invitaions:
            invitaion = invitaions[0]
            invitaion.status = Invitation.ACCEPTED
            invitaion.save()

            team = invitaion.team
            team.members.add(user = request.user)
            team.save()

            userprofile = request.user.userprofile
            userprofile.active_team_id = team.id
            userprofile.save()

            messages.info(request, 'Invitaion Accepted')

            send_invitaion_accepted(team, invitaion)
            return redirect('team-detail', team_id =team.id)
        else:
            messages.info(request, 'Invitaion was not found')
    
    else:
        return render(request,'userprofile/accept_invitaion.html')