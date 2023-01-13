import os
import sys
from flask import Flask, request

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

from dataUpTest import views