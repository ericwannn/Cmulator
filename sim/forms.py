from django import forms
from .models import SimulationConfig


class SimulationConfigForm(forms.ModelForm):

    class Meta:
        model = SimulationConfig
        fields = ['sim_name', 'author', 'date']
