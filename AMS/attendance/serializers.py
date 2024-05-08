from rest_framework import serializers
from attendance.models import AttendanceLog


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceLog
        fields = "__all__"
