from rest_framework import serializers
from .models import Users
from django.contrib.auth import authenticate

# class MobilesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mobiles
#         fields = '__all__'
#         # fields = {'title','content'}
# from rest_framework import serializers
# from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','firstname' ,'lastname' ,'username', 'email', 'user_type', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users.create_user(validated_data['firstname'],validated_data['lastname'],validated_data['username'], validated_data['email'],validated_data['user_type'], validated_data['password'])

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
