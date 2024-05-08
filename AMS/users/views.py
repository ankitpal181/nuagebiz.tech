from rest_framework.views import APIView
from rest_framework.response import Response
from attendance.models import Users, Students
from users.filters import UserFilters, StudentFilters
from users.serializers import UserSerializer, StudentSerializer
from AMS.utilities import Logger, handle_view_exceptions


# Create your views here.
class UserView(APIView):
    """View class providing CRUD operation apis for user module.
    """
    def __init__(self, **kwargs) -> None:
        self.logger = Logger("users", "user")
        super().__init__(**kwargs)

    def get(self, request) -> list:
        """Fetch user's details from database.
        A single user data will be returned if id is given in request else all users.

        Args:
            request: Django request object.
        
        Returns:
            (list): List of user data
        """
        try:
            # Fetch user data and apply required filters
            users = Users.objects
            filtered_response = UserFilters(data=request.query_params, queryset=users).qs

            # Return serialized response
            serialized_response = UserSerializer(filtered_response, many=True)
            return Response(serialized_response.data)
        except Exception as ex:
            return handle_view_exceptions(self, ex, "users:user")

    def post(self, request) -> Users:
        """Add a new user in database.

        Args:
            request: Django request object, containing new user's details.
        
        Returns:
            (Users): New user's details.
        """
        try:
            # Create a new user record.
            new_user = UserSerializer(data=request.data, partial=True)
            new_user.is_valid(raise_exception=True)
            new_user.save()

            # Return serialized response
            return Response(new_user.data)
        except Exception as ex:
            return handle_view_exceptions(self, ex, "users:user")

    def put(self, request, id: int) -> Users:
        """Update user's details in database.

        Args:
            request: Django request object, containing updation details.
        
        Returns:
            (Users): Updated user data
        """
        try:
            # Get user obejct or raise error if does not exists
            user = Users.objects.filter(id=id).last()

            if user is None:
                raise Exception("No such user exists", "custom")
            
            # Update user data
            updated_user = UserSerializer(user, data=request.data, partial=True)
            updated_user.is_valid(raise_exception=True)
            updated_user.save()

            # Return serialized response
            return Response(updated_user.data)
        except Exception as ex:
            return handle_view_exceptions(self, ex, "users:user")


class StudentView(APIView):
    """View class providing CRUD operation apis for student module.
    """
    def __init__(self, **kwargs) -> None:
        self.logger = Logger("users", "student")
        super().__init__(**kwargs)

    def get(self, request) -> list:
        """Fetch student's details from database.
        A single student data will be returned if id is given in request else all students.

        Args:
            request: Django request object.
        
        Returns:
            (list): List of strudent data
        """
        try:
            # Fetch student data and apply required filters
            students = Students.objects
            filtered_response = StudentFilters(data=request.query_params, queryset=students).qs

            # Return serialized response
            serialized_response = StudentSerializer(filtered_response, many=True)
            return Response(serialized_response.data)
        except Exception as ex:
            return handle_view_exceptions(self, ex, "users:student")

    def post(self, request) -> Students:
        """Add a new student in database.

        Args:
            request: Django request object, containing new student's details.
        
        Returns:
            (Students): New student's details.
        """
        try:
            # Create a new student record.
            new_student = StudentSerializer(data=request.data, partial=True)
            new_student.is_valid(raise_exception=True)
            new_student.save()

            # Return serialized response
            return Response(new_student.data)
        except Exception as ex:
            return handle_view_exceptions(self, ex, "users:student")

    def put(self, request, id: int) -> Students:
        """Update student's details in database.

        Args:
            request: Django request object, containing updation details.
        
        Returns:
            (Students): Updated student data
        """
        try:
            # Get student obejct or raise error if does not exists
            student = Students.objects.filter(id=id).last()

            if student is None:
                raise Exception("No such student exists", "custom")
            
            # Update student data
            updated_student = StudentSerializer(student, data=request.data, partial=True)
            updated_student.is_valid(raise_exception=True)
            updated_student.save()

            # Return serialized response
            return Response(updated_student.data)
        except Exception as ex:
            return handle_view_exceptions(self, ex, "users:student")
