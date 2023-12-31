from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from bot.service.repository import Repo


class DbMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["update", "error"]

    def __init__(self, pool):
        super(DbMiddleware, self).__init__()
        self.pool = pool

    async def pre_process(self, obj, data, *args):
        db = await self.pool.acquire()
        data["db"] = db
        data["repo"] = Repo(db)

    async def post_process(self, obj, data, *args):
        del data["repo"]
        db = data.get("db")
        if db:
            await self.pool.release(db)
