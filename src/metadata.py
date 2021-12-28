import os
from typing import TypeVar, Type
from utils import get_dotenv
from datetime import date as datelib
from dataclasses import dataclass
from dotenv import load_dotenv

M = TypeVar('M', bound='Metadata')

@dataclass (eq=True, frozen=True)
class Metadata:
    token: str
    api_url: str
    location: str
    date: str

    @classmethod
    def load_environment(cls: Type[M]) -> M:
        dotenv_path = get_dotenv()
        load_dotenv(dotenv_path=dotenv_path)
        token = os.getenv('TOKEN')
        api_url = os.getenv('PLANETARY_API_BASE_URL')
        location = os.getenv('COORDINATES')
        date = datelib.today().strftime("%Y-%m-%d")
        return cls(token, api_url, location, date)
