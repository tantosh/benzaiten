from django import forms

class SummaryForm(forms.Form):
    original_text = forms.CharField(label='Text')