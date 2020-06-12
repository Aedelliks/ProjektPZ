from django.contrib import admin

# Register your models here.

from .models import *

admin.site.site_header = "ES Magazyn Administracja"

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
