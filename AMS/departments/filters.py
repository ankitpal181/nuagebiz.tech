import django_filters
from attendance.models import Departments, Courses


class DepartmentFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name="id")
    name = django_filters.CharFilter(field_name="department_name", lookup_expr="contains")
    submitted_by = django_filters.NumberFilter(field_name="submitted_by")

    class Meta:
        model = Departments
        fields = ["id", "name", "submitted_by"]


class CourseFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name="id")
    name = django_filters.CharFilter(field_name="course_name", lookup_expr="contains")
    department = django_filters.NumberFilter(field_name="department_id")
    submitted_by = django_filters.NumberFilter(field_name="submitted_by")

    class Meta:
        model = Courses
        fields = ["id", "name", "department", "submitted_by"]
