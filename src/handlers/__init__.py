from handlers.user.default import user_router
from handlers.admin.default import admin_router

from aiogram import Router
from typing import NoReturn, List

routers: List[Router] = [admin_router, user_router]


def register_handlers(main_router: Router) -> NoReturn:
    for router in routers:
        main_router.include_router(router)
