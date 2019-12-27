from django.forms import ModelForm
from .models import Pessoa


class PessoasForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'