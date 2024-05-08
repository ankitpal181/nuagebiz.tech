import base64
from datetime import datetime
from rest_framework.response import Response
from AMS.serializers import FailureSerializer


def encrypt_data(data: str) -> str:
    return base64.b64encode(data.encode("UTF-8"))

def handle_view_exceptions(class_instance, exception: Exception, error_code: str) -> dict:
    # Prepare serialized failure response
    message = "Something went wrong, try again"

    if len(exception.args) > 1 and exception.args[1] == "custom":
        message = exception.args[0]

    failure_response = FailureSerializer(data={
        "status": 500,
        "message": message,
        "error_code": error_code
    })

    # Mark log entry and return failure response
    if len(exception.args) == 1 or exception.args[1] != "custom":
        class_instance.logger.log(datetime.now(), str(exception))

    failure_response.is_valid()
    return Response(failure_response.data)


class Logger:
    def __init__(self, app: str = "", module: str = "") -> None:
        self.app = app
        self.module = module
    
    def log(self, time: str, msg: str) -> None:
        with open("error_logs.txt", "a+") as file:
            file.write("{} {}:{} {}\n".format(time, self.app, self.module, msg))
