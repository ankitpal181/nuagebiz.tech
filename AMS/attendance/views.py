from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from attendance.models import AttendanceLog
from attendance.filters import AttendanceFilters
from attendance.serializers import AttendanceSerializer
from AMS.serializers import FailureSerializer
from AMS.utilities import Logger


# Create your views here.
class AttendanceView(APIView):
    """View class providing CRUD operation apis for attendance module.
    """
    def __init__(self, **kwargs) -> None:
        self.logger = Logger("attendance", "attendance")
        super().__init__(**kwargs)

    def get(self, request) -> list:
        """Fetch attendance's details from database.
        A single attendance data will be returned if id is given in request else all attendance.

        Args:
            request: Django request object.
        
        Returns:
            (list): List of attendance data
        """
        try:
            # Fetch attendance data and apply required filters
            attendance = AttendanceLog.objects
            filtered_response = AttendanceFilters(
                data=request.query_params, queryset=attendance
            ).qs

            # Return serialized response
            serialized_response = AttendanceSerializer(filtered_response, many=True)
            return Response(serialized_response.data)
        except Exception as ex:
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "attendance:attendance"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)

    def post(self, request) -> AttendanceLog:
        """Add a new attendance in database.

        Args:
            request: Django request object, containing new attendance's details.
        
        Returns:
            (AttendanceLog): New attendance's details.
        """
        try:
            # Create a new attendance record.
            new_attendance = AttendanceSerializer(data=request.data, partial=True)
            new_attendance.is_valid(raise_exception=True)
            new_attendance.save()

            # Return serialized response
            return Response(new_attendance.data)
        except Exception as ex:
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "attendance:attendance"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)

    def put(self, request, id: int) -> AttendanceLog:
        """Update attendance's details in database.

        Args:
            request: Django request object, containing updation details.
        
        Returns:
            (AttendanceLog): Updated attendance data
        """
        try:
            # Get attendance obejct or raise error if does not exists
            attendance = AttendanceLog.objects.filter(id=id).last()

            if attendance is None:
                raise Exception("No such attendance record exists", "custom")
            
            # Update attendance data
            updated_attendance = AttendanceSerializer(attendance, data=request.data, partial=True)
            updated_attendance.is_valid(raise_exception=True)
            updated_attendance.save()

            # Return serialized response
            return Response(updated_attendance.data)
        except Exception as ex:
            # Prepare serialized failure response
            message = "Something went wrong, try again"

            if len(ex.args) > 1 and ex.args[1] == "custom":
                message = ex.args[0]

            failure_response = FailureSerializer(data={
                "status": 500,
                "message": message,
                "error_code": "attendance:attendance"
            })

            # Mark log entry and return failure response
            if len(ex.args) > 1 and ex.args[1] == "custom":
                self.logger.log(datetime.now(), str(ex))

            failure_response.is_valid()
            return Response(failure_response.data)
