from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer



class CustomLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # print(attrs)
        # print(data)
        user = User.objects.get(email = attrs['email']) 
        data["id"] = user.id
        data["is_teacher"] = user.is_teacher
        return data



class RegisterSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'email', 'username', 'password',
            'password_confirm' 
        ] 

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email already exists')
        return email

    def validate(self, attrs):
        p1 = attrs['password']
        p2 = attrs.pop('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError(
                'Passwords does not match'
            )
        return attrs

    def create(self, validated_data):
        print('CREATING USER WITH DATA:', validated_data)
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "date_joined", "about")

    


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "date_joined", "about", "is_teacher")
        
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['full_name'] = instance.first_name + ' ' + instance.last_name
        # print(instance.student.name, '!!!!!!!!!!!@!')

        return repr



    
   
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "about")
