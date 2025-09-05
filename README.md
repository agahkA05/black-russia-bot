# Black Russia Market Bot

Telegram бот для торговли в игре Black Russia.

## Функции

- 🔍 Поиск товаров по категориям
- 📝 Размещение объявлений
- ⭐ Система избранного
- 💬 Чат с продавцами
- 📊 Аналитика и статистика
- 🔔 Уведомления
- 👑 Админ-панель
- 🖥️ Поддержка всех серверов Black Russia

## Установка

1. Клонируйте репозиторий
2. Установите зависимости: `pip install -r requirements.txt`
3. Настройте переменные окружения
4. Запустите бота: `python main.py`

## Деплой на Railway

1. Создайте аккаунт на [Railway.app](https://railway.app)
2. Подключите GitHub репозиторий
3. Нажмите "Deploy"
4. Бот будет работать 24/7

## Переменные окружения

- `BOT_TOKEN` - токен Telegram бота
- `ADMIN_USERNAME` - username администратора

## Структура проекта

```
├── main.py              # Главный файл
├── config.py            # Конфигурация
├── handlers.py          # Обработчики
├── keyboards.py         # Клавиатуры
├── keyboards_extended.py # Дополнительные клавиатуры
├── database.py          # База данных
├── states.py            # FSM состояния
├── requirements.txt     # Зависимости
├── Procfile            # Конфигурация для Railway
└── README.md           # Документация
```

## Лицензия

MIT License