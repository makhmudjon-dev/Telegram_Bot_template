from typing import Union, List, NoReturn

from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdminFilter(BaseFilter):
    def __init__(self, admins_list: Union[str, List]) -> NoReturn:
        self.ADMINS = admins_list

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.ADMINS, List):
            return message.from_user.id in [int(id) for id in self.ADMINS]
