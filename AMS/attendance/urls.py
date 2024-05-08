from django.urls import path
from attendance.views import AttendanceView

urlpatterns = [
    path('', AttendanceView.as_view()),
    path('<int:id>/', AttendanceView.as_view())
]
