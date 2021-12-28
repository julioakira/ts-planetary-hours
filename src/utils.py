from pathlib import Path

def get_project_root() -> Path:
  return Path.cwd()

def get_dotenv() -> Path:
  return get_project_root() / '.env'
