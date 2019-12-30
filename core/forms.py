from django.forms import ModelForm, forms
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista


class PessoasForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'



class VeiculosForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'



class RotativosForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'



class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'



class MovMensalForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'

