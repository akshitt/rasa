from flask import Flask, render_template, url_for, flash, redirect, request
from flaskblog import app, db

#!-----------------------------------------------------------------------------------------------------

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', title= 'Home')
#!------------------------------------------------------------------------------------------------
