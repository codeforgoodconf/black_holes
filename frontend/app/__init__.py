from flask import Flask

app = Flask(__name__)
from app import views

from scripts.seeds import seed_db

seed_db()