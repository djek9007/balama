from django.forms import  ModelForm

from organizations.models import Organization
from django_select2 import forms as s2forms



class  OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = Organization.objects.none()


