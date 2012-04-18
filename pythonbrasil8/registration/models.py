# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    name = models.CharField(_('Nome Completo'), max_length=100)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Celular'), max_length=20)
    cpf = models.CharField(_('CPF'), max_length=11)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    hash = models.CharField(_('Hash'), max_length=40, null=True, blank=True)
