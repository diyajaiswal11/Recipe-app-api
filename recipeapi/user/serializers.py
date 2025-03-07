from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializers for user objects"""

    class Meta:
        model= get_user_model()
        fields=(
            'email','password','name'
        )
        extra_kwargs ={'password':{'write_only':True, 'min_length': 5 }}

 
    def create(self,validated_data):
        """Create new user with encrypted password and return it"""

        return get_user_model().objects.create_user(**validated_data)



class AuthTokenSerializer(serializers.Serializer):
    """serializer for user authentication object"""
    email=serializers.CharField()
    password=serializers.CharField(
        style= {'input_type': 'password'},
        trim_whitespace=False
    )


    def validate(self,attrs):
        """validate and authenticate user"""
        email=attrs.get('email')
        password=attrs.get('password')
        




