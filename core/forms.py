from django.forms import ModelForm
from .models import Pessoa, Veiculo


class PessoasForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'



class VeiculosForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'