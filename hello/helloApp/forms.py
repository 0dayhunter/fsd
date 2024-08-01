from django.forms import ModelForm
from helloApp.models import project

class projectForm(ModelForm):
    class Meta:
        model=project
        fields=['student','ptitle','plang','pduration']