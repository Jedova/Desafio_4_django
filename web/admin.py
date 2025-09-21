from django.contrib import admin
from .models import Flan, ContactForm

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display  = ("name", "slug", "is_private")
    list_filter   = ("is_private",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)} 

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display  = ("customer_name", "customer_email", "contact_form_uuid")
    search_fields = ("customer_name", "customer_email")