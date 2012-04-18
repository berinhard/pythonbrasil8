# coding: utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase

from ..forms import SubscriptionForm


class Registration(TestCase):

    def test_show_registration_form(self):
        response = self.client.get(reverse('registration:form'))
        self.assertTemplateUsed(response, 'registration/subscription_form.html')

    def test_subscription_form_is_present(self):
        response = self.client.get(reverse('registration:form'))
        self.assertIsInstance(response.context['form'], SubscriptionForm)

    def test_submit_valid_subscription(self):
        data = dict(name='Dorneles Tremea', email='deo@tremea.com', cpf='11111111111', phone='21-98989898')
        response = self.client.post(reverse(('registration:form')), data=data)
        self.assertRedirects(response, reverse('registration:checkout', args=[None]))

    def test_empty_subscription_is_invalid(self):
        response = self.client.post(reverse(('registration:form')), data={})
        self.assertTemplateUsed(response, 'registration/subscription_form.html')