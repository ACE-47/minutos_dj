
from django.urls import path
from . import views
urlpatterns = [
    path('add-team/',views.add_team, name='add-team'),
    path('<int:team_id>/team-detail/',views.team_detail, name='team-detail'),
    path('edit-team/',views.edit_team, name='edit-team'),
    path('<int:team_id>activate-team/',views.activate_team, name='activate-team'),
    ]