from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from attendance.models import Users, Students
from users.filters import UserFilters, StudentFilters
from users.serializers import UserSerializer, StudentSerializer
from AMS.serializers import FailureSerializer
from AMS.utilities import Logger


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
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "users:user"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)

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
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "users:user"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)

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
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "users:user"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)


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
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "users:student"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)

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
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "users:student"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)

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
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "users:student"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)
