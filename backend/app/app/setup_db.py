from tortoise import Tortoise, run_async

from app.core.config import DATABASE_URL
from app.models.tortoise.user import User_DB
from app.api.dependencies.authentication import get_password_hash


async def setup_db():
    await Tortoise.init(
        db_url=str(DATABASE_URL),
        modules={'models': ['app.models.tortoise.task', 'app.models.tortoise.user']}
    )
    await Tortoise.generate_schemas()
    await User_DB.get_or_create(username='admin', hashed_password=get_password_hash('123456'))
    # currently a new database record for "admin:123456" will be generated each time the app starts, 
    # because "hashed_password" always varies. 
    await Tortoise.close_connections()


if __name__ == '__main__':
    run_async(setup_db())
