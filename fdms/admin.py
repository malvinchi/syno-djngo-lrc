from django.contrib import admin

# Register your models here.
from .models import Institutions, Beneficiary, Securities

class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('benef_name', 'benef_contact') # the variable name is a keyword. cannot change is be mis-spelt
    search_fields = ('benef_name', "benef_contact")

admin.site.register(Institutions)
admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Securities)
