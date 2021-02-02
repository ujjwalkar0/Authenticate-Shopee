from rest_framework import serializers
from app.models import *
from users.models import *

######--------Profile ---------#########

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = '__all__' # ['username','first_name','last_name', 'email', 'user_type']

####################################################


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CatagoriessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagoriess
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
