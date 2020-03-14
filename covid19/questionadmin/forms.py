from django import forms

class ScaleForm(forms.Form):
    CHOICES = [
            (0, 'None'),
            (1, 'Mild'),
            (2, 'Moderate'),
            (3, 'Severe'),
            ]
    scale = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
