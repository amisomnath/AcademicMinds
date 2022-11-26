from rest_framework.exceptions import APIException, NotFound


class BaseCustomAPIException(APIException):
    custom_code = None
    additional_fields = []

    def __init__(self, *args, **kwargs):
        for field in self.additional_fields:
            setattr(self, field, kwargs.pop(field))
        if self.custom_code is None:
            raise ValueError('custom_code is not set for {}'. format(self.__name__))
        super().__init__(*args, **kwargs)

    def get_detail_data(self) -> dict:
        detail_data = {field: getattr(self, field) for field in self.additional_fields}
        return detail_data


class StudentNotExistsException(NotFound, BaseCustomAPIException):
    custom_code = 404


class SubjectNotExistsException(NotFound, BaseCustomAPIException):
    custom_code = 404
