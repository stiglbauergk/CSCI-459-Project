from django import forms
from animals.models import Animal
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"

