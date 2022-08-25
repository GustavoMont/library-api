from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import user_logged_in, get_user_model
from rest_framework import serializers
from rest_framework.exceptions import APIException

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise APIException("The passwords doens't match")
        return data

    def create(self, data):
        user = UserModel.objects.create_user(
            email=data['email'],
            cpf=data['cpf'],
            last_name=data['last_name'],
            first_name=data['first_name'],
            username=data['username'],
            password=data['password'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ('id','email', 'cpf', 'username', 'first_name', 'last_name', 'password', 'password2')


class LibraryTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validate = super().validate(attrs)
        user_logged_in.send(
            sender=self.user.__class__,
            request=self.context["request"],
            user=self.user,
        )
        return validate

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
         
        # Add custom claims
        token['name'] = user.first_name
        token['full_name'] = user.full_name
        token['id'] = user.id
        token['email'] = user.email
        # ...

        return token


