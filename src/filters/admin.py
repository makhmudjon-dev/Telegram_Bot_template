from typing import Union, List
from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdminFilter(BaseFilter):
    def __init__(self, admins_list: Union[int, List[int], List[str]]):
        if isinstance(admins_list, list):
            self.ADMINS = set(map(int, admins_list))
        elif isinstance(admins_list, int):
            self.ADMINS = {admins_list}

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.ADMINS
