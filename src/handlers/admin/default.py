from typing import NoReturn

from db.model import User
from filters.admin import IsAdminFilter
from keyboards.main import inline_builder, reply_builder

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

admin_router = Router()
from config import ADMINS


@admin_router.message(CommandStart(), IsAdminFilter(ADMINS))
async def default_handler(message: Message, session: AsyncSession, state: FSMContext) -> NoReturn:
    pattern = dict(
        text=f'*ADMIN PANEL*\n\nHello {message.from_user.full_name}',
        reply_markup=inline_builder(
            ["Inline "],
            ["callback"],
            1
        )
    )
    await message.answer(**pattern)
