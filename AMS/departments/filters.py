from django_filters import rest_framework as filters
from attendance.models import Departments, Courses


class DepartmentFilters(filters.FilterSet):
    id = filters.NumberFilter(field_name="id")
    name = filters.CharFilter(field_name="department_name", lookup_expr="contains")
    submitted_by = filters.NumberFilter(field_name="submitted_by")

    class Meta:
        model = Departments
        fields = ["id", "name", "submitted_by"]


class CourseFilters(filters.FilterSet):
    id = filters.NumberFilter(field_name="id")
    name = filters.CharFilter(field_name="course_name", lookup_expr="contains")
    department = filters.NumberFilter(field_name="department_id")
    submitted_by = filters.NumberFilter(field_name="submitted_by")

    class Meta:
        model = Courses
        fields = ["id", "name", "department", "submitted_by"]
