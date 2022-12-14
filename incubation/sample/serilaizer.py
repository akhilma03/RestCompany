from lib2to3.pgen2 import token
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Application
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id','username','email','name','isAdmin',]

    def get_isAdmin(self,obj):
        return obj.is_staff    

    def get_name(self,obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name     

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)    
    class Meta:
        model = User
        fields = ['id','username','email','name','isAdmin','token',]

    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
        

class ApplicationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Application
        fields = '__all__'

class UpdateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Application
        fields = ['AppProcess']        