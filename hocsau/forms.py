from django import forms


class MyForm (forms.Form):
    title = forms.CharField(required=True)
    message = forms.Textarea()