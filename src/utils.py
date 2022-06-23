from pathlib import Path
from typing import Dict
from datetime import date as datelib
import requests
import json
import time

CALENDAR = '\U0001F4C5'
CLOCK = '\U0001F55C'
SPARKLES = '\U00002728'


def get_project_root() -> Path:
  return Path.cwd()

def get_dotenv() -> Path:
  return get_project_root() / '.env'

def get_planetary_hour(base_url: str, date: str, location: str) -> str:
  with requests.get(f"{base_url}/{date}/{location}") as response:
    return json.loads(response.text)

def translate_week_days(week_day: str) -> str:
    return {
        'Monday': 'Segunda-feira',
        'Tuesday': 'Terça-feira',
        'Wednesday': 'Quarta-feira',
        'Thursday': 'Quinta-feira',
        'Friday': 'Sexta-feira',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo',
    }.get(week_day, f'Não foi possível traduzir o dia: {week_day}')

def translate_regents(regent: str) -> str:
    return {
        'Mars': 'Marte',
        'Venus': 'Vênus',
        'Mercury': 'Mercúrio',
        'Moon': 'Lua',
        'Sun': 'Sol',
        'Saturn': 'Saturno',
        'Jupiter': 'Júpiter',
    }.get(regent, f'Não foi possível traduzir o regente: {regent}')

def parse_day(response: Dict)-> str:
    resp = response['Response']['General']
    today_date = datelib.today()
    #todo: fix spacing in first line
    return f"""

    {SPARKLES}{SPARKLES}{SPARKLES}
    {CALENDAR} Data da Consulta: {today_date.strftime('%d/%m/%Y')}
    
    {CLOCK} Hora da Consulta: {time.strftime('%H:%M:%S')}
    
    {CALENDAR} Dia da Semana: {translate_week_days(resp['DayoftheWeek'])}
    
    Regente do Dia: {translate_regents(resp['PlanetaryRuler'])}
    {SPARKLES}{SPARKLES}{SPARKLES}

    """