from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

fuel = [('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Electric', 'Electric'), ('LPG', 'LPG')]
seller_type_ = [('Dealer', 'Dealer'), ('Individual', 'Individual'), ('Trustmark 0', 'Trustmark 0')]
transmission_ = [('Manual', 'Manual'), ('Automatic', 'Automatic')]
owner_ = [('First Owner', 'First Owner'), ('Second Owner', 'Second Owner'), ('Third Owner', 'Third Owner'), ('Fourth & Above Owner', 'Fourth & Above Owner'), ('Test Drive Car', 'Test Drive Car')]

class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True)
    fields = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    
    image1 = models.ImageField(upload_to="items")
    image2 = models.ImageField(upload_to="items", null=True)
    image3 = models.ImageField(upload_to="items", null=True)
    image4 = models.ImageField(upload_to="items", null=True)
    image5 = models.ImageField(upload_to="items", null=True)

    catagory = models.ForeignKey(Categories, on_delete=models.CASCADE)
    stock = models.IntegerField()
    price = models.IntegerField()
    desc = RichTextField()
    post_date = models.DateField(auto_now_add=True,)
    Pin_No = models.IntegerField()

    others = models.TextField(null=True, blank=True)

    # released_year = models.IntegerField(null=True, )
    # km_driven = models.IntegerField(null=True, )
    # fuel_type = models.CharField(null=True, choices=fuel, max_length=255)
    # seller_type = models.CharField(null=True, max_length=255)
    # transmission = models.CharField(null=True, max_length=255)
    # owner = models.CharField(null=True, max_length=255)
    # author = models.CharField(max_length=255, null=True)
    # author_desc = RichTextField(null=True)

    def __str__(self):
        return self.title
