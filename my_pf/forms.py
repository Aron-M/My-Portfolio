from django import forms
from .models import PersonalDetails, Headings, Skills, Project


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = '__all__'

class HeadingsForm(forms.ModelForm):
    class Meta:
        model = Headings
        fields = '__all__'
        widgets = {
            'big_header': forms.Textarea(attrs={'rows':3, 'cols': 70}),
            'sub_header': forms.Textarea(attrs={'rows':3, 'cols': 70}),
            'par1': forms.Textarea(attrs={'rows': 3, 'cols': 70}),
            'par2': forms.Textarea(attrs={'rows': 3, 'cols': 70}),
            'par3': forms.Textarea(attrs={'rows': 3, 'cols': 70}),
            'par4': forms.Textarea(attrs={'rows': 3, 'cols': 70}),
        }

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'description', 'github_url']