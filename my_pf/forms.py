from django import forms
from .models import PersonalDetails, Headings


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = '__all__'

class HeadingsForm(forms.ModelForm):
    class Meta:
        model = Headings
        fields = '__all__'
        widgets = {
            'big_header': forms.Textarea(attrs={'rows':4, 'cols': 40}),
            'sub_header': forms.Textarea(attrs={'rows':4, 'cols': 40}),
            'par1': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'par2': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'par3': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'par4': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
