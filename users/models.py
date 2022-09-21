from django.db import models
from django.contrib.auth.models import User

class Users(User):
    user_type = models.CharField(max_length=50, choices=[('Business', 'Business'), ('Delivery Boy', 'Delivery Boy'), ('Customer', 'Customer')]) 
        
    def create_user(first_name, last_name, username, email=None, user_type='None', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not username:
            raise ValueError('The given username must be set')
        
        email = Users.objects.normalize_email(email)
        username = Users.objects.model.normalize_username(username)
        user = Users.objects.model(first_name=first_name, last_name=last_name, username=username, email=email, user_type=user_type,**extra_fields)
       
        user.set_password(password)
        user.save(using=Users.objects._db)
        print(password)
        return user
    
