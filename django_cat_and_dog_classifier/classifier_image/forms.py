from django import forms
from ..test_page.models import PetClassifier

class PetClassifierForm(forms.ModelForm):
    class Meta:
        model = PetClassifier
        fields = ['image', 'label']
