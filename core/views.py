from django.shortcuts import render

from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
import os
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.


def home(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            send_mail(
                contact.subject,
                "Confirmation Email for " + contact.email + " with phone number " + contact.phone + ".",
                os.environ.get('EMAIL_HOST_USER'),
                [contact.email],
                fail_silently=False,
            )
            form = ContactForm()
            messages.success(request, 'Your message has been sent!')
            return redirect('home')

    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'core/home.html', context)