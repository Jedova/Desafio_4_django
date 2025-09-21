from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import ContactForm as ContactFormModel

class ContactFormModelForm(ModelForm):
    class Meta:
        model  = ContactFormModel
        fields = ["customer_email", "customer_name", "message"]
        widgets = {
            "customer_email": forms.EmailInput(attrs={"class": "form-control"}),
            "customer_name":  forms.TextInput(attrs={"class": "form-control"}),
            "message":        forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }

    def clean_customer_email(self):
        email = self.cleaned_data["customer_email"]
        domain = email.split("@")[-1].lower()

        try:
            import dns.resolver
            answers = dns.resolver.resolve(domain, "MX")
            if not answers:
                raise ValidationError(_("El dominio de correo no tiene registros MX válidos."))
        except (ImportError):
            if "." not in domain:
                raise ValidationError(_("Dominio de correo inválido."))
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
            raise ValidationError(_("No se encontraron registros MX para el dominio."))

        return email
