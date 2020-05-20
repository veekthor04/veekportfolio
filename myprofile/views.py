from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import os
CONTACT_MAIL = os.getenv('CONTACT_MAIL')

# Create your views here.
def my_profile(request):
    context = {
    }
    return render(request, "my_profile.html", context)

def contact(request):
    if request.method == 'POST':
        name="none"
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        msg = request.POST['msg']
        message = f'Name: {name},\n\n' \
		f'Phone Number: {phone},\n\n' \
        f'Email: {email},\n\n' \
		f'Message: {msg}'
        subject = "Private Message"
        try:
            send_mail(subject, message, email, [CONTACT_MAIL])
        except BadHeaderError:
            messages.info(request, 'Invalid header found.')
            return render(request, "contact.html")
        messages.info(request, 'Your message has been sent successfully!')
        return render(request, "contact.html")
    context = {
    }
    return render(request, "contact.html", context)
