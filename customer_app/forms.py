from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    """
    Form for capturing customer information and uploading an Excel file.

    Fields:
        excel_file (FileField): The Excel file containing financial data.
    """
    excel_file = forms.FileField()

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'date_of_birth', 'excel_file']
        widgets = {
            'date_of_birth': forms.TextInput(attrs={'id': 'id_date_of_birth'}),
        }
        
    
    def clean_excel_file(self):
        excel_file = self.cleaned_data.get('excel_file')
        if not excel_file.name.endswith('.xls') and not excel_file.name.endswith('.xlsx'):
            raise forms.ValidationError('Only Excel files are allowed.')
        return excel_file