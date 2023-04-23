from django.contrib import admin
from .models import Contact, Course, MailingList, Unit, Topic, CourseRegistration, Bundle, GlobalConfig, BundleRegistration, SaleMessage


# Register your models here.


admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(MailingList)
admin.site.register(Unit)
admin.site.register(Topic)
admin.site.register(CourseRegistration)
admin.site.register(Bundle)
admin.site.register(GlobalConfig)
admin.site.register(BundleRegistration)
admin.site.register(SaleMessage)
