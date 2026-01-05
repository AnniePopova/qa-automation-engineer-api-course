import asyncio
import websockets


async def client():
    uri = "ws://localhost:8765"  # Адрес сервера

    async with websockets.connect(uri) as websocket:
        # Отправляем одно сообщение
        message = "Привет, сервер!"
        print(f"Отправка: {message}")
        await websocket.send(message)

        # Получаем 5 ответных сообщений
        for i in range(5):
            response = await websocket.recv()
            print(f"Ответ {i + 1}: {response}")


if __name__ == "__main__":
    asyncio.run(client())

