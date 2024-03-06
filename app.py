from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyPlugin

from src.endpoints.auth import register_handler, login_handler
from src.endpoints.roles import assign_role_handler, remove_role_handler
from src.auth import jwt_auth
from src.db import db_config
from src.dependencies import provide_transaction

app = Litestar(
    [register_handler, login_handler, assign_role_handler, remove_role_handler],
    on_app_init=[jwt_auth.on_app_init],
    dependencies={"transaction": provide_transaction},
    plugins=[SQLAlchemyPlugin(db_config)],
)
