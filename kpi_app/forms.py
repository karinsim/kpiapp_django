from django.forms import ModelForm
from .models import Circle, Kpi


class KPIForm(ModelForm):
    class Meta:
        model = Kpi
        fields = ["value", "month", "year"]
