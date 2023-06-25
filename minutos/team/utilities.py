from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_invitaion(to_email, code, team):
    from_email = settings.DEFAULT_EMAIL_FROM
    acceptation_url = settings.ACCEPTATION_URL
    
    subject = 'Invitaion to Minutos'
    text_content = 'Invitaion to Minutos. Your Code is %s' % code
    html_content = render_to_string('team/email_invitaion.html',{'acceptation_url':acceptation_url,'code':code, ' team':team})

    msg = EmailMultiAlternatives(subject, text_content,from_email,[to_email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


def send_invitaion_accepted(team, to_email,invitaion):
    from_email = settings.DEFAULT_EMAIL_FROM

    subject = 'Invitaion Accepted'
    text_content = 'Your Invitaion was accepted'
    html_content = render_to_string('team/email_accepted.html',{'team':team, 'invitaion':invitaion})

    msg = EmailMultiAlternatives(subject,text_content,from_email,[to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()