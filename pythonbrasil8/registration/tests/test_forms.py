# coding: utf-8
from django.test import TestCase

from ..forms import SubscriptionForm


def subscription_form(d):
    '''Helper to initialize and validate a SubscriptionForm.'''
    f = SubscriptionForm(d)
    f.is_valid()
    return f


class SubscriptionFormTestCase(TestCase):

    def test_excluded_fields_are_not_present(self):
        form =  SubscriptionForm()
        self.assertNotIn('created_at', form.fields)
        self.assertNotIn('hash', form.fields)

    def test_required_fields(self):
        form = subscription_form({})
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone', form.errors)
        self.assertIn('cpf', form.errors)

    def test_cpf_must_have_11_digits(self):
        form = subscription_form({'cpf': '123456789'})
        self.assertIn('cpf', form.errors)

    def test_cpf_have_only_numeric_digits(self):
        form = subscription_form({'cpf': '123456789A'})
        self.assertIn('cpf', form.errors)

    def test_cpf_must_be_valid(self):
        # Invalid
        form = subscription_form({'cpf': '12345678901'})
        self.assertIn('cpf', form.errors)

        # Valid
        form = subscription_form({'cpf': '32844513743'})
        self.assertNotIn('cpf', form.errors)

    def test_name_must_have_at_least_2_words(self):
        form = subscription_form({'name': 'Dorneles'})
        self.assertIn('name', form.errors)
