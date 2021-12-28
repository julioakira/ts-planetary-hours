from pathlib import Path
import requests
import json

def get_project_root() -> Path:
  return Path.cwd()

def get_dotenv() -> Path:
  return get_project_root() / '.env'

def get_planetary_hour(base_url: str, date: str, location: str) -> str:
  with requests.get(f"{base_url}/{date}/{location}") as response:
    return json.loads(response.text)