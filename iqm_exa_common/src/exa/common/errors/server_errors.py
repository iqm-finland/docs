# Copyright 2024 IQM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Errors used in the client-server communication."""

from http import HTTPStatus

from exa.common.errors.exa_error import ExaError


class StationControlError(ExaError):
    """Base class for station control errors used in client-server communication."""

    # TODO: StationControlError shouldn't need to inherit ExaError
    #  Some clients might still expect ExaErrors, thus inheriting here to avoid issues because of that.
    #  Ideally, we would keep server errors (raised by station control) and any client side errors separately.


class BadRequestError(StationControlError):
    """Error raised when the request syntax is invalid or the method is unsupported in general."""


class UnauthorizedError(StationControlError):
    """Error raised when the user is not authorized."""


class ForbiddenError(StationControlError):
    """Error raised when the operation is forbidden for the user."""


class NotFoundError(StationControlError):
    """Error raised when nothing was found with the given parameters.

    This should be used when it's expected that something is found, for example when trying to find with an exact ID.
    """


class ValidationError(StationControlError):
    """Error raised when something is unprocessable in general, for example if the input value is not acceptable."""


class InternalServerError(StationControlError):
    """Error raised when an unexpected error happened on the server side.

    This error should never be raised when something expected happens,
    and whenever the client encounters this, it should be considered as a server bug.
    """


class ServiceUnavailableError(StationControlError):
    """Error raised when the service is unavailable."""


ERROR_TO_STATUS_CODE_MAPPING = {
    BadRequestError: HTTPStatus.BAD_REQUEST,  # 400
    UnauthorizedError: HTTPStatus.UNAUTHORIZED,  # 401
    ForbiddenError: HTTPStatus.FORBIDDEN,  # 403
    NotFoundError: HTTPStatus.NOT_FOUND,  # 404
    ValidationError: HTTPStatus.UNPROCESSABLE_ENTITY,  # 422
    InternalServerError: HTTPStatus.INTERNAL_SERVER_ERROR,  # 500
    ServiceUnavailableError: HTTPStatus.SERVICE_UNAVAILABLE,  # 503
}

STATUS_CODE_TO_ERROR_MAPPING = {value: key for key, value in ERROR_TO_STATUS_CODE_MAPPING.items()}
