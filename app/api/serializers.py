from django.contrib.auth.models import User
from rest_framework import serializers

from app.time_control.models import TimeControl


class TimeControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeControl
        fields = ('user', 'start', 'end', 'comment')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
