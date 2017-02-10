from django import forms

class SummaryForm(forms.Form):
    original_text = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':'15', 'cols': '100', 'class': 'form-control'}))
    number_sentences = forms.IntegerField(min_value=1, initial=10)