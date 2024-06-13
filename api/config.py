from pydantic import BaseSettings, validator

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    next_public_auth0_audience: str
    next_public_auth0_domain: str
    next_public_client_origin_url: str
    port: int = 8000
    reload: bool = False

    def auth0_domain(self):
        return f'https://{self.next_public_auth0_domain}/'

    @classmethod
    @validator("next_public_auth0_audience", "next_public_auth0_domain", "next_public_client_origin_url")
    def check_not_empty(cls, v):
        assert v != "", f"{v} is not defined"
        return v

    class Config:
        env_file = ".env.local"
        env_file_encoding = "utf-8"


settings = Settings()
