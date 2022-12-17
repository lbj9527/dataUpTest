import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.venv')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from dataUpTest import app