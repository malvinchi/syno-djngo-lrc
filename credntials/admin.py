from django.contrib import admin

# Register your models here.
from .models import InstType, Institutions, AccHolder, Credntials

admin.site.register(Credntials)
admin.site.register(AccHolder)
admin.site.register(InstType)
admin.site.register(Institutions)
