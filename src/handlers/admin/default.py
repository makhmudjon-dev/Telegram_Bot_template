from keyboards.main import inline_builder
from filters.admin import IsAdminFilter
from typing import NoReturn

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

admin_router = Router()
from config import ADMINS


@admin_router.message(CommandStart(), IsAdminFilter(ADMINS))
async def default_handler(message: Message) -> NoReturn:
    pattern = dict(
        text=f'*ADMIN PANEL*\n\nHello {message.from_user.full_name}',
        reply_markup=inline_builder(
            ["Inline "],
            ["callback"],
            1
        )
    )
    await message.answer(**pattern)
