from keyboards.main import inline_builder

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from typing import NoReturn

default_router = Router()


@default_router.message(CommandStart())
async def default_handler(message: Message) -> NoReturn:
    pattern = dict(
        text=f'Hello {message.from_user.full_name}',
        reply_markup=inline_builder(
                             ["Inline "],
                             ["callback"],
                             1
                         )
    )
    await message.answer(**pattern)
