from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from customer.models import Customer
from products.models import *
from users.models import Users
from business.models import Shop
from products.forms import *
from django.http import JsonResponse
from rest_framework import routers, serializers, viewsets,permissions
from delivery.models import DeliveryAgent
import pandas as pd
import json
from django.conf import settings
import os
import pickle as pk
# from pymongo import MongoClient

value = settings.BASE_DIR

# print(os.listdir(os.path.join(value)))

decode = {
    'Processor': 
        {
            'Intel Core i5 Processor (10th Gen)': 22,
            'Intel Core i3 Processor (11th Gen)': 18,
            'Intel Pentium Quad Core Processor': 37,
            'AMD Athlon Dual Core Processor': 2,
            'AMD Ryzen 5 Quad Core Processor': 9,
            'Intel Core i7 Processor (10th Gen)': 27,
            'Intel Core i3 Processor (10th Gen)': 17,
            'AMD Ryzen 3 Dual Core Processor': 4,
            'Intel Core i5 Processor (9th Gen)': 26,
            'Intel Core i5 Processor (11th Gen)': 23,
            'Intel Celeron Dual Core Processor': 16,
            'Intel Core i7 Processor (9th Gen)': 31,
            'AMD Ryzen 7 Octa Core Processor': 12,
            'AMD Ryzen 5 Hexa Core Processor': 7,
            'Intel Core i7 Processor (11th Gen)': 28,
            'AMD Ryzen 3 Quad Core Processor': 5,
            'Intel Core i5 Processor (8th Gen)': 25,
            'AMD Ryzen 9 Octa Core Processor': 15,
            'AMD Ryzen 5 Quad Core Processor (3rd Gen)': 10,
            'Intel Core i9 Processor (9th Gen)': 34,
            'AMD Ryzen 7 Quad Core Processor': 14,
            'AMD Dual Core Processor': 3,
            'Intel Core i9 Processor (10th Gen)': 32,
            'Intel Core i7 Processor (8th Gen)': 30,
            'AMD Ryzen 5 Dual Core Processor': 6,
            'AMD APU Dual Core A6 Processor': 1,
            'Intel Core i7 Processor (7th Gen)': 29,
            'Microsoft Core i5 Processor (11th Gen)': 38,
            'Intel Core i5 Processor (7th Gen)': 24,
            'Intel Core i9 Processor (8th Gen)': 33,
            'AMD Ryzen 5 Hexa Core Processor (5th Gen)': 8,
            'AMD Ryzen 7 Hexa Core Processor': 11,
            'AMD Ryzen 7 Octa Core Processor (5th Gen)': 13,
            'Intel Evo platform feat 11th Gen Intel Core i5 processor': 35,
            'Intel Evo platform feat 11th Gen Intel Core i7 processor': 36,
            'Intel Core i3 Processor (7th Gen)': 20,
            'Intel Core i3 Processor (5th Gen)': 19,
            'AMD APU Dual Core A4 Processor': 0,
            'Intel Core i3 Processor (8th Gen)': 21
        },
    'RAM': 
        {
            '8 GB DDR4 RAM': 10,
            '4 GB DDR4 RAM': 8,
            '16 GB DDR4 RAM': 2,
            '8 GB LPDDR4X RAM': 12,
            '8 GB LPDDR3 RAM': 11,
            '32 GB LPDDR4X RAM': 6,
            '16 GB LPDDR4X RAM': 4,
            '16 GB LPDDR3 RAM': 3,
            '8 GB DDR3 RAM': 9,
            '16 GB DDR3 RAM': 1,
            '32 GB DDR4 RAM': 5,
            'Upgradable SSD Upto 512 GB and RAM Upto 32 GB': 13,
            '4 GB DDR3 RAM': 7,
            '12 GB DDR4 RAM': 0
        },
    'Operating System': 
        {
            '64 bit Windows 10 Operating System': 1,
            'Mac OS Operating System': 3,
            'Windows 10 Operating System': 5,
            'Pre-installed Genuine Windows 10 Operating System (Includes Built-in Security, Free Automated Updates, Latest Features)': 4,
            'DOS Operating System': 2,
            '64 bit Chrome Operating System': 0
        },
    'Storage':
        {
            '1 TB HDD': 0,
            '256 GB SSD': 8,
            '1 TB HDD|256 GB SSD': 2,
            '512 GB SSD': 10,
            '1 TB SSD': 4,
            'M.2 Slot for SSD Upgrade': 12,
            '128 GB NVMe PCIe 3.0 x4 SSD': 5,
            '1 TB HDD|128 GB SSD': 1,
            '128 GB SSD': 6,
            '512 GB SSD for Reduced Boot Up Time and in Game Loading': 11,
            '1 TB HDD|512 GB SSD': 3,
            '128 GB SSD for Reduced Boot Up Time and in Game Loading': 7,
            '512 GB HDD|512 GB SSD': 9
        },
    'Display': 
        {
            '39.62 cm (15.6 inch) Display': 22,
                '35.56 cm (14 Inch) Display': 14,
                '35.56 cm (14 inch) Display': 16,
                'Matrix Display, Dragon Center, Cooler Boost 5, Nahimic 3': 28,
                '29.46 cm (11.6 inch) Touchscreen Display': 4,
                '33.78 cm (13.3 inch) Display': 9,
                '15.6 inches Full HD IPS Thin Bezel Display (144Hz, 45% NTSC Color Gamut)': 0,
                'SHIFT, SteelSeries Engine 3, Matrix Display (Extend), Dragon Center, GamingMode, VR Ready, Cooler Boost 5, Nahimic 3, Nahimic VR, Giant Speaker': 29,
                '33.78 cm (13.3 inch) Touchscreen Display': 10,
                '15.6 inches Full HD IPS Thin Bezel Display (60Hz, 45% NTSC Color Gamut)': 1,
                '35.56 cm (14 inch) Touchscreen Display': 17,
                '33.02 cm (13 inch) Display': 7,
                '39.62 cm (15.6 Inch) Display': 21,
                '34.04 cm (13.4 inch) Touchscreen Display': 11,
                '40.64 cm (16 inch) Display': 24,
                '31.24 cm (12.3 inch) Touchscreen Display': 6,
                '35.56 cm (14 inches) Touchscreen Display': 19,
                '39.62 cm (15.6 inch) Touchscreen Display': 23,
                '38.1 cm (15 inch) Display': 20,
                '34.54 cm (13.6 inch) Touchscreen Display': 13,
                '43.94 cm (17.3 inch) Display': 25,
                '34.29 cm (13.5 inch) Touchscreen Display': 12,
                '33.78 cm (13.3 Inch) Display': 8,
                'Full HD LED Backlit Display': 27,
                '30.48 cm (12 inch) Touchscreen Display': 5,
                '35.56 cm (14 inches) Display': 18,
                '25.65 cm (10.1 inch) Touchscreen Display': 3,
                'Full HD LED Backlit Anti-glare Display for Better Visual Experience': 26,
                '35.56 cm (14 Inch) Touchscreen Display': 15,
                '25.4 cm (10 inch) Touchscreen Display': 2
        },
    'Warranty': 
        {
            '1 Year Onsite Warranty': 15,
            '2 Year Warranty': 21,
            '1 Year International Travelers Warranty (ITW)': 6,
            '24 Months Warranty': 27,
            '2 Years Carry In Warranty': 24,
            '1 Year Warranty': 18,
            '2 Year Warranty Term for Gaming & Content Creation (EU-WE)': 23,
            '2 Year Warranty Term for Gaming': 22,
            '1 Year International Travelers Warranty': 5,
            '1 Year Domestic Brand Warranty on Device': 4,
            '1 Year Carry-In Warranty': 2,
            '18 Months Warranty + 6 Months Extended Warranty (6 Months Extended Warranty Upon Online Product Registration on www.avita-india.com)': 19,
            '1 Year Limited Warranty': 11,
            '1 Year Limited Hardware Warranty': 7,
            '3 Years Manufacturer Warranty': 33,
            '3 Years Limited Hardware Warranty, In Home Service After Remote Diagnosis - Retail': 32,
            '1 Year Limited Hardware Warranty, In Home Service After Remote Diagnosis - Retail': 8,
            '1 Year Standard Warranty': 17,
            'One-year International Travelers Warranty (ITW)': 35,
            '2 Year Carry-In Warranty': 20,
            '1 Year Onsite Warranty Commencing from the Date of Purchase': 16,
            '1 Year Manufacturer Warranty on the Device from the Date of Purchase': 13,
            '2 Years Onsite Warranty': 25,
            '1 Year Carry In Warranty': 0,
            '3 Year Limited Warranty': 28,
            '3 Year Manufacturer Warranty on the Device and 6 Months Manufacturer Warranty on Included Accessories from the Date of Purchase': 29,
            '1 Year Carry in Warranty': 1,
            '1 Year Manufacturer Warranty on the Device and 6 Months Manufacturer Warranty on Included Accessories from the Date of Purchase': 12,
            '1 Year Limited International Hardware Warranty': 10,
            '3 Years Onsite Warranty': 34,
            '3 Year Premier Support Warranty': 30,
            '1 Year Complete Cover Warranty': 3,
            '3 Years Domestic and 1 Year International Travelers Warranty (ITW)': 31,
            '2 Years Warranty': 26,
            '1 Year Onsite Manufacturing Warranty': 14,
            '1 Year Limited Hardware Warranty, In Home Service After Remote Diagnosis-Retail': 9,
            'Onsite Global Warranty': 36
        }
    }


# print()

class HomeView(ListView):
    model = Product
    template_name = "products/home.html"
    ordering = ['-id']
    paginate_by = 15

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["product_list"] = Product.objects.all()

        hostname = f"http://{self.request.get_host()}/delivery/orders/"
        if self.request.is_secure():
            hostname = f"https://{self.request.get_host()}/delivery/orders/"


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
                    context["products"] = "Product List"
                
                elif (context["user_type"]=="Business"):
                    context["product_list"] = Product.objects.filter(user_id=self.request.user)
                    context["products"] = "Your Product"
                
                elif (context["user_type"]=="Delivery Boy"):
                    accept = f"http://{self.request.get_host()}/orders/accept/"
                    if self.request.is_secure():
                        accept = f"https://{self.request.get_host()}/orders/accept/"

                    context["product_list"] = None
                    context["products"] = ""
                    context["hostname"] = hostname
                    context["accept"] = accept
                    context["deliveryagent_registered"] = len(DeliveryAgent.objects.filter(user_id=self.request.user))!=0
                    context["deliveryagent_id"] = DeliveryAgent.objects.filter(user_id=self.request.user).first().id
            
            except:
                ...
        return context

def predicted_price(request):
    if request.method == "GET":
        return render(request, "products/predict.html", {"form": LaptopForm})
    elif request.method == "POST":
        print(request.POST.get("laptop"))

        new_data = {
                "Processor" : decode["Processor"][request.POST.get("processor")],
                "RAM" : decode["RAM"][request.POST.get("ram")],
                "Operating System":  decode["Operating System"][request.POST.get("os")],
                "Storage" : decode["Storage"][request.POST.get("storage")],
                "Display" : decode["Display"][request.POST.get("display")],
                "Warranty" : decode["Warranty"][request.POST.get("warranty")]
            }

        print(new_data)
        # mongo = MongoClient("mongodb://mongo:27017")

        # mydb = mongo["laptop"]

        # mydb.seats.insert_many(new_data)

        
        test = pd.DataFrame(dict([(i, [j]) for i,j in zip(new_data.keys(), new_data.values())]))

        print(test)
        with open(os.path.join(value, 'models', 'LaptopPricePrediction.pk'), 'rb') as f:
            rfr = pk.load(f)

        predicted_price = round(rfr.predict(test)[0], 2)

        return render(request, "products/predict.html", {"predicted_price": predicted_price})

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/details.html"

    def get_context_data(self, *args, **kwargs):
        

        hostname = f"http://{self.request.get_host()}/orders/add/"
        if self.request.is_secure():
            hostname = f"https://{self.request.get_host()}/orders/add/"

        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)

        context["shop"] = Shop.objects.get(user_id=kwargs["object"].user_id).shop_name
        context["shop_id"] = Shop.objects.get(user_id=kwargs["object"].user_id).id
        context['hostname'] = hostname
        try:
            context["user_type"] = Users.objects.get(id=self.request.user.id).user_type
        except:
            context["user_type"] = None 


        if context["product"].catagory.name=="Laptop":
            try:
                a = json.loads((context["product"].others))
                with open(os.path.join(value, 'models', 'LaptopPricePrediction.pk'), 'rb') as f:
                    rfr = pk.load(f)
                test = pd.DataFrame(dict([(i, [decode[i][j]]) for i, j in zip(a.keys(), a.values())]))
                context["predicted_price"] = round(rfr.predict(test)[0], 2)
            except:
                pass

        if (context["user_type"]=="Customer"):
            context["customer_id"] = Customer.objects.filter(name=self.request.user)[0].id
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
        print(json.loads(Categories.objects.get(id=pk).fields[2:-1]))
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
