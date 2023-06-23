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

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')