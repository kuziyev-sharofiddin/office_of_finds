from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only =True)
    password2 = serializers.CharField(required=True, write_only =True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'is_active',
            'is_superuser',
            'is_staff',
            'password',
            'password2',
        )
        extra_kwargs = {
            'password':{"write_only":True},
            'password2':{"write_only":True},
        }
        
    def create(self, validated_data):
        username = self.validated_data.get('username')
        email = self.validated_data.get("email")
        is_active = self.validated_data.get('is_active')
        is_superuser = self.validated_data.get('is_superuser')
        is_staff = self.validated_data.get('is_staff')
        password = self._validated_data.get("password")
        password2 = self.validated_data.get("password2")
        
        
        if password==password2:
            user = User(username=username, email=email, is_active=is_active, is_superuser=is_superuser, is_staff=is_staff)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError(
                {
                    "error":"Both passwords do not match"
                }
            )

