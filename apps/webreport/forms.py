from django import forms

class URLForm(forms.Form):
    url = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )
