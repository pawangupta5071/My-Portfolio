from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def send_email(request):

    if request.method == 'POST':
        template = render_to_string('base/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(request.POST['subject'], template, settings.EMAIL_HOST_USER, [
                             'pkgupta5071453@gmail.com'])
        email.fail_silently = False
        email.send()
    return render(request, 'base/email_send.html')
