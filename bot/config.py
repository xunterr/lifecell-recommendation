from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list

@dataclass 
class AzureAPIConfig:
    service_name: str
    workspace_name: str
    subscription_id: str
    resource_group: str

@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    azure_api: AzureAPIConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS")))
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        azure_api=AzureAPIConfig(
            service_name=env.str("SERVICE_NAME"),
            workspace_name=env.str("WORKSPACE_NAME"),
            subscription_id=env.str("SUBSCRIPTION_ID"),
            resource_group=env.str("RESOURCE_GROUP")
        )
    )