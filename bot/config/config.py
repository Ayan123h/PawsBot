from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [7200, 10800]
    START_DELAY: list[int] = [5, 25]
    AUTO_TASK: bool = True
    JOIN_TG_CHANNELS: bool = False
    REF_ID: str = 'iFAXjw5j'
    DISABLED_TASKS: list[str] = ['boost']
    CONNECT_TON_WALLET: bool = False
    DISCONNECT_TON_WALLET: bool = False


settings = Settings()
