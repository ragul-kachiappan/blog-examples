from rest_framework import status
from rest_framework.exceptions import APIException


class CustomValidationError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {"result": False, "msg": "Validation Error"}
    default_code = "validation_error"

    def __init__(self, detail=None, code=None):
        if detail:
            self.default_detail["msg"] = detail
        self.detail = self.default_detail
        if code is None:
            code = self.default_code
