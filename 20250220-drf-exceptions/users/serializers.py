from rest_framework import serializers

from users.custom_exceptions import CustomValidationError
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "company_name", "phone_number", "address"]
        extra_kwargs = {
            "username": {"required": False},
            "email": {"required": False},
            "company_name": {"required": False},
            "phone_number": {"required": False},
            "address": {"required": False},
        }

    def validate(self, data: dict):
        required_fields = {
            "username": "username is required",
            "email": "email is required",
            "company_name": "company_name is required",
            "phone_number": "phone_number is required",
            "address": "address is required",
        }

        for field, message in required_fields.items():
            if not data.get(field):
                raise CustomValidationError(detail=message, code="validation_error")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.company_name = validated_data.get(
            "company_name", instance.company_name
        )
        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )
        instance.address = validated_data.get("address", instance.address)
        instance.save()
        return instance
