from rest_framework import serializers
from attendance.models import Users, Students
from AMS.utilities import encrypt_data


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data["password"] = encrypt_data(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = encrypt_data(validated_data["password"])

        return super().update(instance, validated_data)


    class Meta:
        model = Users
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"
