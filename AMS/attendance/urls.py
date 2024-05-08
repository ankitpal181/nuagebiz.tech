from django.urls import path
from departments.views import DepartmentView, CourseView

urlpatterns = [
    path('', DepartmentView.as_view()),
    path('<int:id>/', DepartmentView.as_view()),
    path('course/', CourseView.as_view()),
    path('course/<int:id>/', CourseView.as_view())
]
