import requests
import re
import os
import json
from utils import get_dotenv
from datetime import date
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass (eq=True, frozen=True)
class Auth:
    token: str
    api_url: str
    coordinates: str
    current_date: str

    @classmethod
    def load_environment(cls):
        dotenv_path = get_dotenv()
        load_dotenv(dotenv_path=dotenv_path)
        token = os.getenv('TOKEN')
        api_url = os.getenv('PLANETARY_API_BASE_URL')
        coordinates = os.getenv('COORDINATES')
        current_date = date.today().strftime("%Y-%m-%d")
        return cls(token, api_url, coordinates, current_date)
    
    def retrieve_token(self):
        return self.token
    
    def retrieve_api_url(self):
        return self.api_url
    
    def retrieve_coordinates(self):
        return self.coordinates
    
    def retrieve_date(self):
        return self.current_date

def get_planetary_hour(base_url: str, date: str, location: str) -> str:
    with requests.get(f'{base_url}/{date}/{location}') as response:
        return json.loads(response.text)

def main():
    env = Auth.load_environment()
    response = get_planetary_hour(
    env.retrieve_api_url(),
    env.retrieve_date(),
    env.retrieve_coordinates())
    print(response)

if __name__ == '__main__':
    main()