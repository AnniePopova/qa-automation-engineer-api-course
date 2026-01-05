import socket


def tcp_users_server():
    # История всех сообщений от всех клиентов
    messages = []

    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сервер к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Разрешаем до 10 подключений одновременно
    server_socket.listen(10)
    print("TCP сервер запущен и ожидает подключений...")

    while True:
        # Принимаем подключение от клиента
        client_socket, client_address = server_socket.accept()

        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        # Получаем сообщение от клиента
        data = client_socket.recv(1024).decode()

        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        # Добавляем сообщение в историю
        messages.append(data)

        # Формируем ответ — вся история сообщений
        history = "\n".join(messages)

        # Отправляем историю клиенту
        client_socket.send(history.encode())

        # Закрываем соединение с клиентом
        client_socket.close()


if __name__ == '__main__':
    tcp_users_server()
