import grpc

import user_service_pb2

import user_service_pb2_grpc

class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        print(f'Получен запрос к методу GetUser от пользователя: {request.username}')