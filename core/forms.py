from django import forms
from .models import Contact, Course

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['email', 'subject', 'phone']


    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'emailHelp'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'subjectHelp'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'phoneHelp'})

