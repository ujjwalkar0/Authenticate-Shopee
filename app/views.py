from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import csv, io
from django.contrib import messages
from users.models import *
from .utils import *
# def home(request):
#     return render(request,'home.html',{})

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    
class ProfileView(DetailView):
    model = Profile
    template_name = "profile.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ProfileView,self).get_context_data(*args, **kwargs)
        context["user_type"] = user_type(username=self.request.user)

def profile_upload(request):   
    template = "profile_upload.html"
    data = Phones.objects.all()
    prompt = {
        'profiles': data    
              }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Phones.objects.update_or_create(
            Product_name = column[0],
            by_info = column[1],
            # Product_url = column[2],
            Product_img_link = column[3],
            Product_price = column[4],
            prod_des = column[5],
            feature = column[6],
            cust_review = column[7],

            # name = column[0],
            # year = column[1],
            # selling_price = column[2],
            # km_driven = column[3],
            # fuel = column[4],
            # seller_type = column[5],
            # transmission = column[6],
            # owner = column[7],


        )
    context = {}
    return render(request, template, context)


def view_last_8(products):
    try:
        return products[len(products)-8:]
    except:
        return products

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    # cats = Catagoriess.objects.all()
    ordering = ['-id']
    paginate_by = 15

    def get_context_data(self,*args, **kwargs):
        cat_menu = Catagoriess.objects.all()
        my_phones = Phones.objects.filter(user_id=self.request.user.id)
        my_cars = Car.objects.filter(user_id=self.request.user.id)
        my_products = Post.objects.filter(user_id=self.request.user.id)        
        shop = Shop.objects.filter(user_id=self.request.user.id)
        ip = IP.objects.filter(user_id=self.request.user.id)
        shop_owner = shop_id = None
        # print( " ID :- ",self.request.user.id)
        # print(ip)
        for j in shop:
            shop_owner = j.user_id
            shop_id = j.id
            break
        
        pin_no_by_id=id_by_ip=None

        for j in ip:
            print(j.PIN_NO)
            pin_no_by_id = j.PIN_NO
            id_by_ip = j.id
            break

        # print(Car.objects.filter(Pin_No=pin_no_by_id))

        phones=view_last_8(Phones.objects.filter(Pin_No=pin_no_by_id))       
        car = view_last_8(Car.objects.filter(Pin_No=pin_no_by_id))
        products=view_last_8(Post.objects.filter(Pin_No=pin_no_by_id))
        all_phones=view_last_8(Phones.objects.all())
        all_car=view_last_8(Car.objects.all())
        all_products=view_last_8(Post.objects.all())
        orders = order.objects.filter(Pin_No=pin_no_by_id)
        # print(pin_no_by_id)

        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["phones"] = phones
        context["my_phones"] = my_phones
        context["cars"] = car
        context["my_cars"] = my_cars
        context["my_products"] = my_products
        context["user_type"] = user_type(self.request.user)
        context["shop_owner"] = shop_owner
        context["all_phones"] = all_phones
        context["all_cars"] = all_car
        context["all_products"] = all_products
        context["shop_id"] = shop_id
        context["pin_no_by_id"] = id_by_ip
        context["products"] = products
        context["orders"] = reversed(list(orders))
        context["is_paginated"] = True
        return context

def notifications(request):
    context = {
        'Posts': order.objects.all(),
    }
    return render(request,'myy_posts.html',context)

class MyOrderView(UpdateView):
    model = order
    form_class = OrderForm
    template_name = "order_details.html"

def product_view(name,id):
    if name=="mobiles":
        return Phones.objects.filter(id=id)
    elif name=="Cars":
        return Car.objects.filter(id=id)
    else:
        return Post.objects.filter(id=id)

class MyOrdersView(ListView):
    model = order
    form_class = OrderForm
    template_name = "my_order_details.html"

    def get_context_data(self,*args, **kwargs):
        my_orders = order.objects.filter(customer_id=self.request.user.id)
        # print(id)
        a=[]
        for i in my_orders:
            try:
                blank,name,id,shop = i.product_id.split('/')
                a.append([product_view(name,id),i])
                # print(product_view(name,id))
            except:
                pass
        print(a)
        context = super(MyOrdersView,self).get_context_data(*args, **kwargs)
        context["my_orders"] = reversed(a)
        return context

def shop_from_product(j,name):
    blank,name,id = j.product_id.split('/')
    try:
        return product_view(name,id)
        # print(product_view(name,id))
    except:
        pass

class SellsView(ListView):
    model = order
    form_class = OrderForm
    template_name = "sells.html"

    def get_context_data(self,*args, **kwargs):
        my_sells = order.objects.all() #filter(customer_id=self.request.user.id)
        # print(id)
        a=[]
        for i in my_sells:
            try:
                blank,name,id,shop = i.product_id.split('/')
                # print(shop)
                # print(type(shop))
                if int(shop)==self.request.user.id:
                    a.append([product_view(name,id),i])
                # print(product_view(name,id))
            except:
                pass
        # print(a)
        context = super(SellsView,self).get_context_data(*args, **kwargs)
        context["my_sells"] = reversed(a)
        return context

        pass
            # print(i)
        #     try:
        #         blank,name,id = i.product_id.split('/')
        #         if name=="mobiles":
        #             mobile.append(id)
        #         elif name=="Cars":
        #             car.append(id)
        #         else:
        #             other.append(id)

        #         # a.append([product_view(name,id),i])
        #         # print(product_view(name,id))
        #     except:
        #         pass
        # context = super(SellsView,self).get_context_data(*args, **kwargs)
        # context["phones"] = [i,(Phones.objects.filter(id=i) for i in mobile[1:])]
        # context["post"] = (Post.objects.filter(id=i) for i in car[1:])
        # context["cars"] = (Car.objects.filter(id=i) for i in other[1:])
        # return context

        # print(self.request.user.id)
        # for i in ():
        #     for j in i:
        #         j.user_id==self.request.user.id

        # for i in (Post.objects.filter(id=i) for i in other[1:]):
        #     for j in i:
        #         print(j.user_id==self.request.user.id)

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

class MobilesDetailView(DetailView):
    model = Phones
    template_name = "article_details.html"

class CarDetailView(DetailView):
    model = Car
    template_name = "article_details.html"

    def get_context_data(self,*args, **kwargs):
        train = pd.DataFrame(list(Car.objects.all().values()))
        test = pd.DataFrame(list(Car.objects.filter(id=self.kwargs['pk']).values()))
        
        context = super(CarDetailView,self).get_context_data(*args, **kwargs)
        context["cars"] = Car.objects.filter(id=self.kwargs['pk'])
        context["predicted_price"] = price_predictor(train,test)
        return context


class AddCatagoryView(CreateView):
    model = Catagoriess
    template_name = "cat.html"  
    fields = "__all__"

    def get_context_data(self,*args, **kwargs):

        users = Users.objects.filter(username=self.request.user)
        for i in users:
            user_type = i.user_type
        
        print(user_type)

        context = super(AddCatagoryView,self).get_context_data(*args, **kwargs)
        context["user_type"] = user_type
        context["is_paginated"] = True
        return context

# class CatagoryView(ListView):
#     model = Catagoriess
#     template_name = "catagories.html"  
#     fields = "__all__"

#     def get_context_data(self,*args, **kwargs):
#         phones = Phones.objects.all()
#         car = Car.objects.all()
#         context = super(HomeView,self).get_context_data(*args, **kwargs)
#         context["cat_menu"] = cat_menu
#         context["phones"] = phones
#         context["cars"] = car
#         context["is_paginated"] = True
#         return context

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def CatagoryView(request,cats):
    if cats=="Mobiles":
        object_list = Phones.objects.all()
        paginator = Paginator(object_list, 60)
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)
        return render(request,'catagories.html',{'cats':cats.title(), 'phones':post_list })
    elif cats=="Cars":
        return render(request,'catagories.html',{'cats':cats.title(), 'cars':Car.objects.all() })
    else:
        catagory_posts = Post.objects.filter(catagory=cats)
        return render(request,'catagories.html',{'cats':cats.title(), 'catagory_posts':catagory_posts })

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    def get_context_data(self,*args, **kwargs):
        # cat_menu = Catagoriess.objects.all()
        users = Users.objects.filter(username=self.request.user)
        # my_phones = Phones.objects.filter(salesman=self.request.user)
        # shop = Shop.objects.filter(username=self.request.user)
        # for j in shop:
            # shop_owner = j.username
            # shop_id = j.id
            # break
        user_type = None
        for i in users:
            user_type = i.user_type
        # a=Phones.objects.all()
        # phones = a[len(a)-8:]
        context = super(AddPostView,self).get_context_data(*args, **kwargs)
        # context["cat_menu"] = cat_menu
        # context["phones"] = phones
        # # context["my_phones"] = my_phones
        # context["cars"] = car
        context["user_type"] = user_type
        # # context["shop_owner"] = shop_owner
        # # context["shop_id"] = shop_id
        # context["is_paginated"] = True
        return context

class MobileAddView(CreateView):
    models = Phones
    form_class = PhonesPostForm
    template_name = "add_phones.html"

    def get_context_data(self,*args, **kwargs):
        users = Users.objects.filter(username=self.request.user)
        user_type = None
        for i in users:
            user_type = i.user_type
        context = super(MobileAddView,self).get_context_data(*args, **kwargs)
        context["user_type"] = user_type
        return context


class CarAddView(CreateView):
    models = Car
    form_class = CarPostForm
    template_name = "add_phones.html"
    
    def get_context_data(self,*args, **kwargs):
        users = Users.objects.filter(username=self.request.user)
        user_type = None
        for i in users:
            user_type = i.user_type
        context = super(CarAddView,self).get_context_data(*args, **kwargs)
        context["user_type"] = user_type
        return context


# class AddHeaderView(UpdateView):
#     model = layout
#     form_class = HeaderForm
#     template_name = "HeaderImage.html"

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update.html"

class UpdateMobilesView(UpdateView):
    model = Phones
    form_class = PhonesPostForm
    template_name = "update.html"

class UpdateCarView(UpdateView):
    model = Car
    # form_class = PhonesPostForm
    form_class = CarPostForm
    # fields = '__all__'
    template_name = "update.html"
    success_url = reverse_lazy('home')

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy('home')

class DeleteMobilesView(DeleteView):
    model = Phones
    template_name = "delete.html"
    success_url = reverse_lazy('home')

class DeleteCarView(DeleteView):
    model = Car
    template_name = "delete.html"
    success_url = reverse_lazy('home')

class UserEditView(UpdateView):
    model = Users
    fields = '__all__'
    # form_class = UserEditForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('editProfile')

    def get_object(self):
        return self.request.user

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# def Orderview(request):
#     form = Orders(request.POST,request.FILES)
#     if form.is_valid():
#         print(form)
#         form.save()
#         form = Orders()
#     context = {
#         'form': form,
#     }
#     system = request.POST.get('system',None)
#     context['system'] = system
#     return render(request,'order.html',context)

class Orderview(CreateView):
    model = order
    fields = '__all__'
    template_name = 'order.html'

    def get_context_data(self,*args, **kwargs):
        users = Users.objects.filter(username=self.request.user)
        system = self.request.POST.get('system',None)
        user_type = None
        for i in users:
            user_type = i.user_type
        context = super(Orderview,self).get_context_data(*args, **kwargs)
        context["user_type"] = user_type
        context['system'] = system
        return context

def order_successful(request):
    return render(request,'order_recieved.html',{})
    
def search(request):
    query = request.GET['query']

    page_number = request.GET.get('page')
    object_list = Paginator(Post.objects.filter(title__icontains=query).order_by('-id'),24).get_page(page_number)
    mobiles_list = Paginator(Phones.objects.filter(Product_name__icontains=query).order_by('-id'),24).get_page(page_number)
    cars_list = Paginator(Car.objects.filter(name__icontains=query).order_by('-id'),24).get_page(page_number)
   
    # paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    params = {
        'query':query,
        'object_list':object_list,
        'mobiles_list':mobiles_list,
        'cars_list':cars_list,
        
        }
    return render(request,"search.html",params)

class ShopCreateViews(CreateView):
    model = Shop
    template_name = "shop.html"
    fields = "__all__"
    success_url = reverse_lazy('home')


class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = "shop.html"
    success_url = reverse_lazy('home')

class IPCreateViews(CreateView):
    model = IP
    template_name = "shop.html"
    fields = "__all__"
    success_url = reverse_lazy('home')


class IPUpdateView(UpdateView):
    model = IP
    form_class = IPForm
    template_name = "shop.html"
    success_url = reverse_lazy('home')


class CarTest(CreateView):
    models = TestCar
    form_class = CarTestForm
    template_name = "ml.html"
    # print(TestCar.objects.all())

    # def get_context_data(self,*args, **kwargs):
    #     print(TestCar.objects.all().last())

def ml_result(request):
    train = pd.DataFrame(list(Car.objects.all().values()))
    test = pd.DataFrame(list(TestCar.objects.all().values()))
    print(price_predictor(train,test))
    res={
        "price":price_predictor(train,test)
    }

    return render(request,'ml_result.html',res)