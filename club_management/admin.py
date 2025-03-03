from django.contrib import admin
from .models import Student, Club, Patron, Membership, Activity, Finance

admin.site.register(Student)
admin.site.register(Club)
admin.site.register(Patron)
admin.site.register(Membership)
admin.site.register(Activity)
admin.site.register(Finance)

