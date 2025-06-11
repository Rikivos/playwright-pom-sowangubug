import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
BROWSER = os.getenv("BROWSER", "chromium")
TIMEOUT = int(os.getenv("TIMEOUT", 30))

EMAIL = os.getenv("EMAIL")       
PASSWORD = os.getenv("PASSWORD")       
