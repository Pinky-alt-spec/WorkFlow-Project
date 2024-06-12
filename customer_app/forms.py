from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    excel_file = forms.FileField()

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'date_of_birth', 'excel_file']