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
        
# class FindsSerializer(serializers.Serializer):
    
#     # name = serializers.CharField(max_length=200)
#     # user = serializers.ForeignKey(User, on_delete=models.CASCADE)
#     # image = serializers.ImageField(upload_to='find_images', blank=True, null=True)
#     # category = serializers.ForeignKey(Category, on_delete=models.CASCADE)
#     # region = serializers.ForeignKey(Region, on_delete=models.CASCADE)
#     # description = serializers.TextField()
#     # status = serializers.BooleanField(default=False)
#     # tag = serializers.CharField(max_length=100, null=True, blank=True)
#     # lost_time = serializers.DateField()
#     # created_at = serializers.DateTimeField(auto_now_add=True)


#     # def create(self, validated_data):
#     #     return FindsSerializer(**validated_data)
    
    
        

# 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