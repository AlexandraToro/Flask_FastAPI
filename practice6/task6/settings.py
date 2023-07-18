from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	DATABASE_URL: str
	MAX_LENGTH_NAME: int = 20
	MAX_LENGTH_SURNAME: int = 100
	MAX_LENGTH_EMAIL: int = 200
	MAX_LENGTH_PASSWORD: int = 128
	MIN_LENGTH_PASSWORD: int = 8

	
	class Config:
		env_file = ".env"


settings = Settings()
