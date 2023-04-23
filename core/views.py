from django.shortcuts import render

from .models import Contact, MailingList, Course, Unit, Topic, Bundle, SaleMessage
from .forms import ContactForm, MailingListForm, CourseRegisterForm, BundleRegisterForm
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
                "Contact Email for " + contact.email + " with phone number " + contact.phone + "." + "\n\n" + contact.description,
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


    courses = Course.objects.filter().order_by('-is_published', )
    featured_courses = Course.objects.filter(is_published=True, is_featured=True)
    bundles = Bundle.objects.filter().order_by('-is_published',)

    sale_message = SaleMessage.objects.first()
    message_flag = False

    while not message_flag:
        for course in courses:
            if course.discount > 0:
                messages.success(request, sale_message.message)
                message_flag = True
        
        for bundle in bundles:
            if bundle.discount > 0:
                messages.success(request, sale_message.message)
                message_flag = True

    context = {
        'form': form,
        'mailing_list_form': mailing_list_form,
        'courses': courses,
        'featured_courses': featured_courses,
        'bundles': bundles,
    }

    return render(request, 'core/home.html', context)


def course(request, slug):


    if request.method == 'POST':
        form = CourseRegisterForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.course = Course.objects.get(slug=slug)
            contact.save()
            send_mail(
                f"Course Registeration Confirmation for {contact.course.name}",
                "Confirmation Email for " + contact.email + " with phone number " + contact.phone + ".\n Course: " + contact.course.name + ".\n We will contact you shortly on whatsapp to confirm your registration and proceed with payment.",
                os.environ.get('EMAIL_HOST_USER'),
                [contact.email],
                fail_silently=False,
            )
            form = CourseRegisterForm()
            messages.success(request, f'You have successfuly registered for {contact.course.name}! We will contact you shortly to proceed with payment!')
            return redirect('home')
        else:
            messages.warning(request, 'Something went wrong!')
            return redirect('home')

    else:
        form = CourseRegisterForm()

    course = Course.objects.get(slug=slug)
    context = {
        'course': course,
        'form': form,

    }

    return render(request, 'core/course-detail.html', context)


def bundle(request, slug):
    if request.method == 'POST':
        form = BundleRegisterForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.bundle = Bundle.objects.get(slug=slug)
            contact.save()

            send_mail(
                f"Bundle Registeration Confirmation for {contact.bundle.name}",
                "Confirmation Email for " + contact.email + " with phone number " + contact.phone + ".\n Course: " + contact.bundle.name + ".\n We will contact you shortly on whatsapp to confirm your registration and proceed with payment.",
                os.environ.get('EMAIL_HOST_USER'),
                [contact.email],
                fail_silently=False,
            )
            form = BundleRegisterForm()
            messages.success(request, f'You have successfuly registered for {contact.course.name}! We will contact you shortly to proceed with payment!')
            return redirect('home')
        else:
            messages.warning(request, 'Something went wrong!')
            return redirect('home')

    else:
        form = BundleRegisterForm()

    bundle = Bundle.objects.get(slug=slug)
    print(bundle.description)
    context = {
        'bundle': bundle,
        'form': form,
    }

    return render(request, 'core/bundle-detail.html', context)