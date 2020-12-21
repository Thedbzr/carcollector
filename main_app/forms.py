from django.forms import ModelForm
from .models import Tuneup

class TuneupForm(ModelForm):
  class Meta:
    model = Tuneup
    fields = ['date', 'service']