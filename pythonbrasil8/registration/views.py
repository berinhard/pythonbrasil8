# coding: utf-8
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView

from .forms import SubscriptionForm
from .models import Subscription


class RegistrationView(CreateView):
    form_class = SubscriptionForm
    model = Subscription

    def get_success_url(self):
        return reverse('registration:checkout', args=[self.object.hash])


class CheckoutView(TemplateView):
    template_name = 'registration/subscription_checkout.html'