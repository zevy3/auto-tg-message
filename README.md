# Telegram Auto Message Script

Скрипт для отправки сообщений раз в 5 минут с аккаунта.

## Установка

1. Клонируйте репозиторий
2. Установите зависимости:
pip install -r requirements.txt

3. Скопируйте конфиг:
cp config.example.py config.py


4. Отредактируйте `config.py` со своими данными:
- API_ID и API_HASH получите на https://my.telegram.org/auth/auth
- CHAT_ID — ID чата для отправки сообщений

5. Запустите:
python main.py


