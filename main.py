from pyrogram import Client
import asyncio
from config import API_ID,API_HASH,CHAT_ID
# Создаём приложение
app = Client(
    name='my_account',
    api_id=API_ID,
    api_hash=API_HASH
)

async def send_messages():
    async with app:
        while True:
            try:
                await app.send_message(CHAT_ID, ".отн сделать комплимент")
                print("✓ Сообщение отправлено")
            except Exception as e:
                print(f"✗ Ошибка: {e}")
            
            # Ждём 5 минут
            await asyncio.sleep(10)

if __name__ == '__main__':
    asyncio.run(send_messages())
