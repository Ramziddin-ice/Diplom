from django import forms


class NameForm(forms.Form):
    first_text = forms.CharField(widget=forms.Textarea)
    second_text = forms.CharField(widget=forms.Textarea)
