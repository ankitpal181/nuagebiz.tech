import django_filters
from attendance.models import Users, Students


class UserFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name="id")
    name = django_filters.CharFilter(field_name="full_name", lookup_expr="contains")
    username = django_filters.CharFilter(field_name="username", lookup_expr="contains")
    email = django_filters.CharFilter(field_name="email", lookup_expr="contains")
    submitted_by = django_filters.NumberFilter(field_name="submitted_by")

    class Meta:
        model = Users
        fields = ["id", "name", "username", "email", "submitted_by"]


class StudentFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name="id")
    name = django_filters.CharFilter(field_name="full_name", lookup_expr="contains")
    department = django_filters.NumberFilter(field_name="department_id")
    submitted_by = django_filters.NumberFilter(field_name="submitted_by")

    class Meta:
        model = Students
        fields = ["id", "name", "department", "submitted_by"]
