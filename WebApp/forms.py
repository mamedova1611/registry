from django.forms import ModelForm
from .models import *

class VHD_Form(ModelForm):
    class Meta:
        model = VHD
        fields = '__all__'

class FO_Form(ModelForm):
    class Meta:
        model = FO
        fields = '__all__'

class NK_Form(ModelForm):
    class Meta:
        model = NK
        fields = '__all__'

class Bank_Form(ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'

class Predpriyatie_Form(ModelForm):
    class Meta:
        model = Predpriyatie
        fields = '__all__'

class PB_Form(ModelForm):
    class Meta:
        model = PB
        fields = '__all__'

class PVD_Form(ModelForm):
    class Meta:
        model = PVD
        fields = '__all__'

class BS_Form(ModelForm):
    class Meta:
        model = BS
        fields = '__all__'

class FP_Form(ModelForm):
    class Meta:
        model = FP
        fields = '__all__'