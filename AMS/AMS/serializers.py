from rest_framework import serializers


class FailureSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()
    error_code = serializers.CharField()
