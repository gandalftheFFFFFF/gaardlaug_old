

from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea())
