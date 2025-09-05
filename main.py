import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import os

from config import BOT_TOKEN
from handlers import router
from database import Database

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Регистрация роутеров
dp.include_router(router)

# Инициализация базы данных
db = Database("black_russia_market.db")

async def on_startup():
    """Действия при запуске бота"""
    logger.info("Бот запущен!")
    
    # Добавляем базовые интеграции
    integrations = [
        {
            "name": "Официальный чат",
            "url": "https://t.me/black_russia_chat",
            "type": "chat"
        },
        {
            "name": "Официальный сайт",
            "url": "https://blackrussia.com",
            "type": "website"
        },
        {
            "name": "Официальный канал",
            "url": "https://t.me/black_russia_channel",
            "type": "channel"
        }
    ]
    
    for integration in integrations:
        db.add_integration(
            name=integration["name"],
            integration_type=integration["type"],
            url=integration["url"],
            description=""
        )
    
    logger.info("Базовые интеграции добавлены!")

async def on_shutdown():
    """Действия при остановке бота"""
    logger.info("Бот остановлен!")

async def main():
    """Главная функция"""
    # Создаем папку для загрузок
    os.makedirs("uploads", exist_ok=True)
    
    # Запускаем бота
    logger.info("Запуск бота...")
    
    try:
        await on_startup()
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"Ошибка запуска бота: {e}")
    finally:
        await on_shutdown()

if __name__ == "__main__":
    asyncio.run(main())
