from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from attendance.models import Departments, Courses
from departments.filters import DepartmentFilters, CourseFilters
from departments.serializers import DepartmentSerializer, CourseSerializer
from AMS.serializers import FailureSerializer
from AMS.utilities import Logger


# Create your views here.
class DepartmentView(APIView):
    """View class providing CRUD operation apis for department module.
    """
    def __init__(self, **kwargs) -> None:
        self.logger = Logger("departments", "department")
        super().__init__(**kwargs)

    def get(self, request) -> list:
        """Fetch department's details from database.
        A single department data will be returned if id is given in request else all departments.

        Args:
            request: Django request object.
        
        Returns:
            (list): List of department data
        """
        try:
            # Fetch department data and apply required filters
            departments = Departments.objects
            filtered_response = DepartmentFilters(
                data=request.query_params, queryset=departments
            ).qs

            # Return serialized response
            serialized_response = DepartmentSerializer(filtered_response, many=True)
            return Response(serialized_response.data)
        except Exception as ex:
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "departments:department"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)

    def post(self, request) -> Departments:
        """Add a new department in database.

        Args:
            request: Django request object, containing new department's details.
        
        Returns:
            (Departments): New department's details.
        """
        try:
            # Create a new department record.
            new_department = DepartmentSerializer(data=request.data, partial=True)
            new_department.is_valid(raise_exception=True)
            new_department.save()

            # Return serialized response
            return Response(new_department.data)
        except Exception as ex:
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "departments:department"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)

    def put(self, request, id: int) -> Departments:
        """Update department's details in database.

        Args:
            request: Django request object, containing updation details.
        
        Returns:
            (Departments): Updated department data
        """
        try:
            # Get department obejct or raise error if does not exists
            department = Departments.objects.filter(id=id).last()

            if department is None:
                raise Exception("No such department exists", "custom")
            
            # Update department data
            updated_department = DepartmentSerializer(department, data=request.data, partial=True)
            updated_department.is_valid(raise_exception=True)
            updated_department.save()

            # Return serialized response
            return Response(updated_department.data)
        except Exception as ex:
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "departments:department"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)


class CourseView(APIView):
    """View class providing CRUD operation apis for course module.
    """
    def __init__(self, **kwargs) -> None:
        self.logger = Logger("departments", "course")
        super().__init__(**kwargs)

    def get(self, request) -> list:
        """Fetch course's details from database.
        A single course data will be returned if id is given in request else all courses.

        Args:
            request: Django request object.
        
        Returns:
            (list): List of course data
        """
        try:
            # Fetch course data and apply required filters
            courses = Courses.objects
            filtered_response = CourseFilters(data=request.query_params, queryset=courses).qs

            # Return serialized response
            serialized_response = CourseSerializer(filtered_response, many=True)
            return Response(serialized_response.data)
        except Exception as ex:
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "departments:course"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)

    def post(self, request) -> Courses:
        """Add a new course in database.

        Args:
            request: Django request object, containing new course's details.
        
        Returns:
            (Courses): New course's details.
        """
        try:
            # Create a new course record.
            new_course = CourseSerializer(data=request.data, partial=True)
            new_course.is_valid(raise_exception=True)
            new_course.save()

            # Return serialized response
            return Response(new_course.data)
        except Exception as ex:
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "departments:course"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)

    def put(self, request, id: int) -> Courses:
        """Update course's details in database.

        Args:
            request: Django request object, containing updation details.
        
        Returns:
            (Courses): Updated course data
        """
        try:
            # Get course obejct or raise error if does not exists
            course = Courses.objects.filter(id=id).last()

            if course is None:
                raise Exception("No such course exists", "custom")
            
            # Update course data
            updated_course = CourseSerializer(course, data=request.data, partial=True)
            updated_course.is_valid(raise_exception=True)
            updated_course.save()

            # Return serialized response
            return Response(updated_course.data)
        except Exception as ex:
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "departments:course"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)
