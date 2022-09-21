from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from customer.models import Customer
from products.models import *
from users.models import Users
from business.models import Shop
from products.forms import ProductForm
from django.http import JsonResponse
from rest_framework import routers, serializers, viewsets,permissions

import json

class HomeView(ListView):
    model = Product
    template_name = "products/home.html"
    ordering = ['-id']
    paginate_by = 15

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView,self).get_context_data(*args, **kwargs)

        context["product_list"] = Product.objects.all()

        print(self.request.user.is_authenticated)

        if self.request.user.is_authenticated:
            print(self.request.user)

            context["shop_already_exist"] = len(Shop.objects.filter(user_id=self.request.user))!=0

            if (context["shop_already_exist"]):
                context["shop_id"] = Shop.objects.filter(user_id=self.request.user).first().id

            try:
                context["user_type"] = Users.objects.get(id=self.request.user.id).user_type
                if (context["user_type"]=="Customer"):
                    context["product_list"] = Product.objects.filter(Pin_No=Customer.objects.get(name=self.request.user).pin_no)
                    context["customer_registered"] = len(Customer.objects.filter(name=self.request.user))
                    context["customer_id"] = Customer.objects.filter(name=self.request.user)[0].id
                if (context["user_type"]=="Business"):
                    context["product_list"] = Product.objects.filter(user_id=self.request.user)
            except:
                ...
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        context["shop"] = Shop.objects.get(user_id=kwargs["object"].user_id).shop_name
        context["shop_address"] = Shop.objects.get(user_id=kwargs["object"].user_id).address

        context["user_type"] = Users.objects.get(id=self.request.user.id).user_type
        if (context["user_type"]=="Customer"):
            context["user_address"] = Customer.objects.filter(name=self.request.user)[0].address
            context["product_id"] = self.kwargs['pk']

        return context

class NewProduct(CreateView):
    form_class = ProductForm
    template_name = "products/new_product.html"
    success_url = "/"

    def get_context_data(self,*args, **kwargs):

        hostname = f"http://{self.request.get_host()}/category_more_details/"
        if self.request.is_secure():
            hostname = f"https://{self.request.get_host()}/category_more_details/"

        context = super(NewProduct,self).get_context_data(*args, **kwargs)
        context['hostname'] = hostname
        return context

    def form_valid(self, form):            
        user = Users.objects.get(username=self.request.user)
        form.instance.user_id = user
        form.instance.Pin_No = Shop.objects.get(user_id=user).Pin_No
        return super().form_valid(form)

class UpdateProductView(UpdateView): 
    model = Product
    template_name = "products/update.html"
    form_class = ProductForm
    success_url = "/"

class DeleteProductView(DeleteView):
    model = Product
    template_name = "products/delete.html"
    success_url = "/"

    # def get_context_data(self, **kwargs):
    #     context = super(UpdateProductView, self).get_context_data(**kwargs)


def product_category(request):
    if request.method == "GET":
        hostname = f"http://{request.get_host()}/add_category/"
        if request.is_secure():
            hostname = f"https://{request.get_host()}/add_category/"

        return render(request, 'product_category/create.html',{"hostname": hostname})

    if request.method == "POST":
        print(request.body) 
        body = json.loads(request.body)
        Categories.objects.create(name=body["name"], fields=request.body).save()
        return JsonResponse({"msg":"success"})
    

def get_category_details(request, pk):
    if request.method == "GET":
        return JsonResponse(json.loads(Categories.objects.get(id=pk).fields[2:-1]))

def new_product(request):
    if request.method == "GET":
        hostname = f"http://{request.get_host()}/category_more_details/"
        if request.is_secure():
            hostname = f"https://{request.get_host()}/category_more_details/"

        return render(request, 'products/new_product.html', {'form': ProductForm(), "hostname":hostname })
    if request.method == "POST":
        print(request.POST)

    #     cat_menu = Categoriess.objects.all()
    #     my_phones = Phones.objects.filter(user_id=self.request.user.id)
    #     my_cars = Car.objects.filter(user_id=self.request.user.id)
    #     my_products = Post.objects.filter(user_id=self.request.user.id)        
    #     shop = Shop.objects.filter(user_id=self.request.user.id)
    #     ip = IP.objects.filter(user_id=self.request.user.id)
    #     shop_owner = shop_id = None
    #     # print( " ID :- ",self.request.user.id)
    #     # print(ip)
    #     for j in shop:
    #         shop_owner = j.user_id
    #         shop_id = j.id
    #         break
        
    #     pin_no_by_id=id_by_ip=None

    #     for j in ip:
    #         print(j.PIN_NO)
    #         pin_no_by_id = j.PIN_NO
    #         id_by_ip = j.id
    #         break

    #     # print(Car.objects.filter(Pin_No=pin_no_by_id))

    #     phones=view_last_8(Phones.objects.filter(Pin_No=pin_no_by_id))       
    #     car = view_last_8(Car.objects.filter(Pin_No=pin_no_by_id))
    #     products=view_last_8(Post.objects.filter(Pin_No=pin_no_by_id))
    #     all_phones=view_last_8(Phones.objects.all())
    #     all_car=view_last_8(Car.objects.all())
    #     all_products=view_last_8(Post.objects.all())
    #     orders = order.objects.filter(Pin_No=pin_no_by_id)
    #     # print(pin_no_by_id)

    #     context = super(HomeView,self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     context["phones"] = phones
    #     context["my_phones"] = my_phones
    #     context["cars"] = car
    #     context["my_cars"] = my_cars
    #     context["my_products"] = my_products
    #     context["user_type"] = user_type(self.request.user)
    #     context["shop_owner"] = shop_owner
    #     context["all_phones"] = all_phones
    #     context["all_cars"] = all_car
    #     context["all_products"] = all_products
    #     context["shop_id"] = shop_id
    #     context["pin_no_by_id"] = id_by_ip
    #     context["products"] = products
    #     context["orders"] = reversed(list(orders))
    #     context["is_paginated"] = True
    #     return context
