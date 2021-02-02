from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class order(models.Model):
    product_id = models.CharField(max_length=255,null=True)
    customer_id = models.IntegerField(null=True)
    dboy_id = models.IntegerField(null=True,blank=True)
    # is_approved = models.BooleanField(default=False,null=True)
    address = models.CharField(max_length=255,null=True,blank=True,)
    quantity = models.IntegerField(null=True)
    Pin_No = models.IntegerField(null=True)
    Phone_No = models.IntegerField(null=True)
    messages = models.TextField(default=None,max_length=255,null=True,blank=True,)
    Delivery_Charge = models.IntegerField(null=True)

    def get_absolute_url(self):
        return reverse('home')

class TestCar(models.Model):
    year = models.IntegerField()
    km_driven = models.IntegerField()
    fuel = models.CharField(max_length=255)
    seller_type = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('car-ml-res')

class IP(models.Model):
    user_id = models.IntegerField(null=True,blank=True)
    PIN_NO = models.IntegerField(null=True,blank=True)

class Phones(models.Model):
    Product_name = models.TextField(max_length=255,null=True,blank=True,)
    user_id = models.IntegerField(null=True,blank=True)
    by_info = models.TextField(max_length=255,null=True,blank=True,)
    # Product_url = models.TextField(max_length=255,null=True,blank=True,)
    Product_img_link = models.CharField(max_length=255,null=True,blank=True,)
    image = models.ImageField(upload_to="items",null=True, blank=True)
    Product_price = models.TextField(max_length=255,null=True,blank=True,)
    prod_des = models.TextField(max_length=255,null=True,blank=True,)
    feature = models.TextField(max_length=255,null=True,blank=True,)
    cust_review = models.TextField(max_length=255,null=True,blank=True,)
    Pin_No = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.Product_name
    def get_absolute_url(self):
        return reverse('home')

class Car(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    user_id = models.IntegerField(null=True,blank=True)
    image_link = models.CharField(max_length=255,null=True,blank=True)  
    image = models.ImageField(upload_to="items",null=True, blank=True)
    year = models.IntegerField(null=True,blank=True)
    selling_price = models.IntegerField(null=True,blank=True)
    km_driven = models.IntegerField(null=True,blank=True)
    fuel = models.CharField(max_length=255,null=True,blank=True)
    seller_type = models.CharField(max_length=255,null=True,blank=True)
    transmission = models.CharField(max_length=255,null=True,blank=True)
    owner = models.CharField(max_length=255,null=True,blank=True)
    Pin_No = models.IntegerField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse('home')

class Catagoriess(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

class Profile(User):
    image = models.ImageField(null=True,blank=True, upload_to="profile/")
    bio = models.TextField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True,)
    mobile_no = models.CharField(max_length=10,null=True,blank=True,)
    website_url = models.CharField(max_length=255,null=True,blank=True,)
    facebook_url = models.CharField(max_length=255,null=True,blank=True,)
    twitter_url = models.CharField(max_length=255,null=True,blank=True,)
    linkdin_url = models.CharField(max_length=255,null=True,blank=True,)

class Shop(models.Model):
    # user_id = models.IntegerField()
    user_id = models.CharField(max_length=255,default=0)
    shop_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    website = models.CharField(max_length=255,blank=True,null=True)
    Pin_No = models.IntegerField(null=True,blank=True)
    # Subscription = models.CharField(max_length=255,blank=True,null=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True)
    # models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to="items",null=True, blank=True)
    image2 = models.ImageField(upload_to="items",null=True, blank=True)
    catagory = models.CharField(max_length=50,default='Uncatagories') 
    stock = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    body = RichTextField(blank=True,null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True,null=True)
    Pin_No = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        # return reverse('article-details',args=(str(self.id)))
        return reverse('home')

class Review(models.Model):
    post = models.ForeignKey(Post, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = RichTextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)