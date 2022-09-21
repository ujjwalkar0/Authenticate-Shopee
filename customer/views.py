from curses.ascii import US
from django.shortcuts import render
from django.views.generic import *
from customer.models import Customer
from customer.forms import RegisterCustomerForm
from users.models import Users

class RegisterCustomerView(CreateView):
    model = Customer
    form_class = RegisterCustomerForm
    template_name = "customer/register_customer.html"
    success_url = "/"

    def form_valid(self, form):
        user = Users.objects.get(username=self.request.user)
        form.instance.name = user
        return super().form_valid(form)

class UpdateCustomerView(UpdateView):
    model = Customer
    form_class = RegisterCustomerForm
    template_name = "customer/update_customer.html"
    success_url = "/"

    def form_valid(self, form):
        user = Users.objects.get(username=self.request.user)
        form.instance.name = user
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super(UpdateCustomerView, self).get_context_data(*args, **kwargs)
        context["permissions"] = len(Customer.objects.filter(name = Users.objects.get(username=self.request.user)))!=0

        return context