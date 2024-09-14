from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_sqlalchemy import flask_sqlalchemy
from dotenv import load_dotenv
import os


app = Flask(__name__)

username = os.getenv("USERNAME")
password = os.getenv("Password")
database = os.getenv("DB")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@localhost:3000/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)