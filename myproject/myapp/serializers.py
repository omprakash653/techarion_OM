from rest_framework import serializers
from .models import productMainModel,getproduct,userProfileModel

class productMainModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=productMainModel
        fields=['id','unique_code','Title','Description','Price']

class getproductSerializer(serializers.ModelSerializer):
    Product=serializers.CharField(source='Product.Title')
    
    class Meta:
        model = getproduct
        fields=['id','Product']

class userProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=userProfileModel
        fields=['Name','Date_of_birth','Gender_Choice']
