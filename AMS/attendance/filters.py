from django_filters import rest_framework as filters
from attendance.models import AttendanceLog


class AttendanceFilters(filters.FilterSet):
    id = filters.NumberFilter(field_name="id")
    student = filters.NumberFilter(field_name="student_id")
    course = filters.NumberFilter(field_name="course_id")
    submitted_by = filters.NumberFilter(field_name="submitted_by")

    class Meta:
        model = AttendanceLog
        fields = ["id", "student", "course", "submitted_by"]
