import asyncio
import websockets
from websockets import ServerConnection


async def handle_user(websocket: ServerConnection):
    # Цикл обработки входящих сообщений от клиента
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        # Отправляем 5 ответных сообщений
        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)
            await asyncio.sleep(0.1)  # небольшая пауза, чтобы отправка была поэтапной


async def main():
    print("Запуск WebSocket сервера на ws://localhost:8765...")

    # Запускаем WebSocket-сервер
    async with websockets.serve(handle_user, "localhost", 8765):
        print("Сервер запущен. Ожидание подключений...")
        await asyncio.Future()  # вечный блок, чтобы сервер работал


if __name__ == "__main__":
    asyncio.run(main())
