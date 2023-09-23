
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 150, required = False)
    first_name = serializers.CharField(max_length = 150)
    last_name = serializers.CharField(max_length = 150)
    email = serializers.EmailField(required = True,
                                   validators =  [UniqueValidator(queryset= User.objects.all())]
                                   )
    password_1 = serializers.CharField(required = True, write_only = True)
    password_2 = serializers.CharField(required = True, write_only = True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password_1', 'password_2')
        
        extra_kwargs = {
            'first_name' : {'required' : True},
            'last_name' : {'required' : True},
        }
        
    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError({'password': 'passwords did not match'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            password = validated_data['password_1'],
        )
        
        #user.set_password(validated_data['password_1'])
        #user.save()
        return user
