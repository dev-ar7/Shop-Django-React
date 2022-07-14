from django.core import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import validate_password
from pkg_resources import require
from rest_framework import serializers
from .models import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False},
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False}}
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def validate(self, data):
        password = data.get('password')
        errors = dict()

        try:
            password_validation.validate_password(password=password, user=User)
        except exceptions.ValidationError as ve:
            errors['password'] = list(ve)

        if errors:
            raise serializers.ValidationError(errors)
        
        return super(UserSerializer, self).validate(data)
    
    def create_user(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['phone', 'address', 'city', 'state', 'zipcode']


class ChangePasswordSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')