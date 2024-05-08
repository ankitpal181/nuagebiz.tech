import django_filters
from attendance.models import AttendanceLog


class AttendanceFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name="id")
    student = django_filters.NumberFilter(field_name="student_id")
    course = django_filters.NumberFilter(field_name="course_id")
    submitted_by = django_filters.NumberFilter(field_name="submitted_by")

    class Meta:
        model = AttendanceLog
        fields = ["id", "student", "course", "submitted_by"]
