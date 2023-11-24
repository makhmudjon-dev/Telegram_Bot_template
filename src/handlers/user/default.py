from keyboards.main import inline_builder
from typing import NoReturn

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


user_router = Router()


@user_router.message(CommandStart())
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
