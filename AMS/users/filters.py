from django_filters import rest_framework as filters
from attendance.models import Users, Students


class UserFilters(filters.FilterSet):
    id = filters.NumberFilter(field_name="id")
    name = filters.CharFilter(field_name="full_name", lookup_expr="contains")
    username = filters.CharFilter(field_name="username", lookup_expr="contains")
    email = filters.CharFilter(field_name="email", lookup_expr="contains")
    submitted_by = filters.NumberFilter(field_name="submitted_by")

    class Meta:
        model = Users
        fields = ["id", "name", "username", "email", "submitted_by"]


class StudentFilters(filters.FilterSet):
    id = filters.NumberFilter(field_name="id")
    name = filters.CharFilter(field_name="full_name", lookup_expr="contains")
    department = filters.NumberFilter(field_name="department_id")
    submitted_by = filters.NumberFilter(field_name="submitted_by")

    class Meta:
        model = Students
        fields = ["id", "name", "department", "submitted_by"]
