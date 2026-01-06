"""
API клиент для работы с публичными методами эндпоинта /api/v1/users.
"""

from typing import TypedDict
import httpx

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами /api/v1/users.

    Используется для операций, не требующих авторизации,
    например, для создания пользователя.
    """

    def create_user_api(self, request: CreateUserRequestDict) -> httpx.Response:
        """
        Метод выполняет создание нового пользователя.

        :param request: Словарь с данными пользователя:
                        email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post("/api/v1/users", json=request)
