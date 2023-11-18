from aiogram import Bot
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeAllPrivateChats

from typing import NoReturn

async def set_default_commands(bot: Bot) -> NoReturn:
    commands = [
        BotCommand(command="/start", description="Start bot"),
        BotCommand(command="/help", description="Help"),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
