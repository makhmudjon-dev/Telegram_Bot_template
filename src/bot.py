from db import Base
from handlers import register_handlers
from utils.set_bot_commands import set_default_commands

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from asyncio import run
from pathlib import Path
from loguru import logger
from dotenv import load_dotenv


async def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent

    load_dotenv(base_dir / '.env')
    logger.add(base_dir / 'logs.log', level="INFO")

    import config

    engine = create_async_engine(config.DB_URL, echo=False)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())
    bot: Bot = Bot(config.BOT_TOKEN)
    register_handlers(dp)

    logger.info('Bot started')
    await set_default_commands(bot)
    await dp.start_polling(bot)
    logger.info('Bot stopped')


if __name__ == '__main__':
    run(main())
