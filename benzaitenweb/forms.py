from django import forms

class SummaryForm(forms.Form):
    original_text = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':'10', 'class': 'form-control'}))
    number_sentences = forms.IntegerField(min_value=1)