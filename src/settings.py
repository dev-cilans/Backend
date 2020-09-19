import os
from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    TODO:
    disable verbose in production
    """

    load_dotenv(verbose=True)
    app_name: str = "Youtube NLP Backend"
    api_key: str = os.getenv("API_KEY")


settings = Settings()
