from django.urls import path
from users.views import UserView, StudentView

urlpatterns = [
    path('', UserView.as_view()),
    path('<int:id>/', UserView.as_view()),
    path('student/', StudentView.as_view()),
    path('student/<int:id>/', StudentView.as_view())
]
