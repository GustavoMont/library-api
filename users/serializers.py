from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import user_logged_in
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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


