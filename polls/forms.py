from django.forms import ModelForm
from .models import Spisok

class SpisokForm(ModelForm):
    class Meta:
        model = Spisok
        fields = ['doc_ready','doc_TXT','doc_title','doc_specification','doc_note','doc_text']