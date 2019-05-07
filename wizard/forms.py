from django import forms
class FormStepOne(forms.Form):
    CHOICES=[('select1','select 1'), ('select2','select 2')]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class FormStepTwo(forms.Form):
    job = forms.CharField(max_length=100)
    salary = forms.CharField(max_length=100)
    job_description = forms.CharField(widget=forms.Textarea)
