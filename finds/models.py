from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100, unique =True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)

class Region(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
    

class Finds(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='find_images', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default=False)
    tag = models.CharField(max_length=100, null=True, blank=True)
    lost_time = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
    
    # def __str__(self):
    #     return str(self.name)
