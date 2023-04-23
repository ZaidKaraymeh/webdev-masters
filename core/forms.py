from django import forms
from .models import Contact, MailingList, CourseRegistration, BundleRegistration

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['email', 'subject', 'phone', 'course']


    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'emailHelp'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'subjectHelp'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'phoneHelp'})
        self.fields['course'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'courseHelp'})


class CourseRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'emailHelp'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'phoneHelp'})
        
    class Meta:
        model = CourseRegistration
        fields = ["email", "phone"]

class BundleRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'emailHelp'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'phoneHelp'})
        
    class Meta:
        model = BundleRegistration
        fields = ["email", "phone"]


class MailingListForm(forms.ModelForm):
    
        class Meta:
            model = MailingList
            fields = ['email']
    
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'emailHelp'})