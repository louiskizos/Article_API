from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



class AgentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields =  ('username', 'email', 'password')

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields =  ('username', 'password')
        
class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Article 
        fields = '__all__'

class NewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = New
        fields = '__all__'
