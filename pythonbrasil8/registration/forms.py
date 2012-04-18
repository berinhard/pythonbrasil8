# coding: utf-8
from django import forms
from django.utils.translation import gettext as _
from django.contrib.localflavor.br.forms import BRCPFField

from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    cpf = BRCPFField()

    class Meta:
        model = Subscription
        exclude = ('hash', 'created_at')

    def clean_name(self):
        value = self.cleaned_data['name']

        words = value.split()
        if len(words) <= 1:
            raise forms.ValidationError(_(u'Insira o nome completo.'))

        return value