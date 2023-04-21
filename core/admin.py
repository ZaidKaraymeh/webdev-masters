from django.contrib import admin
from .models import Contact, Course, MailingList, Unit, Topic


# Register your models here.


admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(MailingList)
admin.site.register(Unit)
admin.site.register(Topic)