from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "company_name", "phone_number", "address"]

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

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_phone_number(self, value):
        if not value:
            raise serializers.ValidationError("Phone number is required")
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits")
        if len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError(
                "Phone number must be between 10 and 15 digits"
            )
        return value

    def validate_company_name(self, value):
        if not value:
            raise serializers.ValidationError("Company name is required")
        if len(value) < 3:
            raise serializers.ValidationError(
                "Company name must be at least 3 characters long"
            )
        return value

    def validate_address(self, value):
        if not value:
            raise serializers.ValidationError("Address is required")
        if len(value) < 10:
            raise serializers.ValidationError(
                "Address must be at least 10 characters long"
            )
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long"
            )
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "Password must contain at least one number"
            )
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter"
            )
        return value

    def validate_confirm_password(self, value):
        if value != self.initial_data.get("password"):
            raise serializers.ValidationError("Passwords do not match")
        return value
