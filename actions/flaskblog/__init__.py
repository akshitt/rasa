from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
#!--------------------------------------------------------------------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fe8a028d74aa4501203b3cc679d7e424'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#!--------------------------------------------------------------------------------------

db = SQLAlchemy(app)
#!--------------------------------------------------------------------------------------

from flaskblog import routes 
