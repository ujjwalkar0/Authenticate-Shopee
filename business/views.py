from django.shortcuts import render
from business.forms import ShopForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Users
from business.models import Shop
from django.shortcuts import redirect
from django.views.generic import RedirectView

class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = "business/register_shop.html"
    success_url = reverse_lazy('home')

class ShopCreateView(LoginRequiredMixin, CreateView):
    form_class = ShopForm
    template_name = "business/register_shop.html"
    success_url = "/"
    # success_url = reverse_lazy('home', success_url = reverse_lazy('home',kwargs = {'pk': 'idnumber'}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["already_exist"] = len(Shop.objects.filter(user_id=self.request.user))!=0 # Return True if exist
    
        if (context["already_exist"]):
            context["shop_id"] = Shop.objects.filter(user_id=self.request.user).first().id
    
        return context

    def form_valid(self, form):
        if len(Shop.objects.filter(user_id=self.request.user))!=0:
            redirect(f'register_shop/{self.request.user.id}')
            
        user = Users.objects.get(username=self.request.user)
        form.instance.user_id = user
        return super().form_valid(form)

