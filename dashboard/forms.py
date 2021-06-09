from django import forms
from .models import Requisition, Performer, RequisitionAnswer, Answer


class ActCreateForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = ('number', 'receive_date', 'antennas_weight', 'telekom_weight', 'akb_weight', 'iron_weight', 'cable_weight', 'city', 'document')
        widgets = {
            'number': forms.TextInput(attrs={'class':'form-control border-input', 'required':'required'}),
            'receive_date' : forms.DateInput(format='%Y-%d-%m', attrs={'type': 'date', 'class':'form-control border-input', 'required':'required'}),
            'antennas_weight': forms.NumberInput(attrs={'class':'form-control border-input', 'required':'required'}),
            'telekom_weight': forms.NumberInput(attrs={'class':'form-control border-input', 'required':'required'}),
            'akb_weight': forms.NumberInput(attrs={'class':'form-control border-input', 'required':'required'}),
            'iron_weight': forms.NumberInput(attrs={'class':'form-control border-input', 'required':'required'}),
            'cable_weight': forms.NumberInput(attrs={'class':'form-control border-input', 'required':'required'}),
            'city': forms.TextInput(attrs={'class':'form-control border-input', 'required':'required'}),
            'document': forms.FileInput(attrs={'class':'form-control border-input', 'required':'required'}),
        }

class ChoosePerformerForm(forms.ModelForm):
    class Meta:
        model = RequisitionAnswer
        fields = ('requisition', 'performer')
        widgets = {
            'requisition': forms.Select(attrs={'class':'form-control border-input', 'required':'required'}),
            'performer': forms.Select(attrs={'class':'form-control border-input', 'required':'required'}),
        }


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('performer_document',)
        widgets = {
            'performer_document': forms.FileInput(attrs={'class':'form-control border-input', 'required':'required'}),
        }

class CustomerInitiatorForm(forms.ModelForm):
    class Meta:
        model = RequisitionAnswer
        fields = ('initiator_name', 'initiator_phone', 'initiator_representative',)
        widgets = {
            'initiator_name': forms.TextInput(attrs={'class':'form-control border-input', 'required':'required'}),
            'initiator_phone': forms.TextInput(attrs={'class':'form-control border-input', 'required':'required'}),
            'initiator_representative': forms.TextInput(attrs={'class':'form-control border-input', 'required':'required'}),
        }


