from typing import Union, List
from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdminFilter(BaseFilter):
    def __init__(self, ADMINS: Union[int, List[int]]):
        self.ADMINS = set(map(int, ADMINS))

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.ADMINS
