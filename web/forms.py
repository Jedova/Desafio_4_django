from django import forms

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    customer_name  = forms.CharField(
        label="Nombre",
        max_length=64,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    message        = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4})
    )
