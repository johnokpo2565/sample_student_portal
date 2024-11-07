from .models import ProfilePics
from django.forms import ModelForm

class ProfilePicsForm(ModelForm):
    class Meta:
        model = ProfilePics
        fields = ('attachment', )