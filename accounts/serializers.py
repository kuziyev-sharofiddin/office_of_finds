from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("first_name","last_name", "phone_number",  'username', 'password', "is_active")



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only =True)

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            'username',
            "last_name",
            'phone_number',
            'password',
        )
        extra_kwargs = {
            'password':{"write_only":True},
        }
        
    def create(self, validated_data):
        first_name = self.validated_data.get("first_name")
        username = self.validated_data.get("username")
        last_name = self.validated_data.get("last_name")
        phone_number = self.validated_data.get("phone_number")
        password = self._validated_data.get("password")
        
        
        user = CustomUser( first_name=first_name, last_name=last_name, username=username, phone_number=phone_number, password=password)
        user.set_password(password)
        user.save()
        return user
