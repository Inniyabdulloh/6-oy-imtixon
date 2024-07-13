from django.contrib import admin
from .models import Contacts, Products, Services, Reviews
# Register your models here.

admin.site.register(Contacts)
admin.site.register(Products)
admin.site.register(Services)
admin.site.register(Reviews)