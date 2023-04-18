from django.shortcuts import render

from .models import Contact, MailingList
from .forms import ContactForm, MailingListForm
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

        mailing_list_form = MailingListForm(request.POST)
        if mailing_list_form.is_valid():
            email = mailing_list_form.save(commit=False)
            if MailingList.objects.filter(email=email.email).exists():
                messages.warning(request, 'You are already on our mailing list!')
                return redirect('home')
            email.save()
            messages.success(request, 'You have been added to our mailing list!')
            return redirect('home')
    else:
        form = ContactForm()
        mailing_list_form = MailingListForm()

    context = {
        'form': form,
        'mailing_list_form': mailing_list_form
    }

    return render(request, 'core/home.html', context)