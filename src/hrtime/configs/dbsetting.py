from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class DBCRED(BaseSettings):

    user: str
    password: SecretStr
    host: str
    database: str

    model_config = SettingsConfigDict(env_file='.env',
                                      extra='ignore',
                                      env_file_encoding='utf-8')


# if __name__ == '__main__':
#     dbcred = DBCRED()
#     print(dbcred.password.get_secret_value())
