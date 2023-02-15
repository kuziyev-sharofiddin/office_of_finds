from .models import *
from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"
        
        
class FindsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    region = RegionSerializer()
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Finds
        fields = "__all__"