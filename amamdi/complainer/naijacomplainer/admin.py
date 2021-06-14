from django.contrib import admin
from .models import Complainer
# Register your models here.


class ComplainerAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('user', 'date', 'time', 'firstname', 'lastname', 'state', 'complaintIsAgainst', 'natureOfComplaint', 'complaint',)
=======
    list_display = ('user', 'date', 'firstname', 'lastname', 'state', 'complaintIsAgainst', 'natureOfComplaint', 'complaint',)
>>>>>>> github/master


admin.site.site_header = "Complain Nigeria"
admin.site.register(Complainer, ComplainerAdmin)
