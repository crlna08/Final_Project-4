from flask import Flask, jsonify, render_template, request, redirect
import pymongo
from flask_pymongo import PyMongo
import pandas as pd
import json
# From initdb import create_collection

#################################################
# Flask Setup
#################################################
# Instantiate a Flask object at __name__, and save it to a variable called app
app = Flask(__name__)

#################################################
# Database Setup
#################################################
# setup mongo connection
mongo = pymongo.MongoClient("mongodb+srv://tesspalan:YSPTuqMosY6PxoXu@cluster0.dhjfw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = mongo['climate-dashboard']

#################################################
# Flask Routes
#################################################
# index route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tiktok")
def visualizations():
    return render_template("tiktok.html")

@app.route("/spotify")
def data():
    return render_template("spotify.html")

@app.route("/trends")
def data():
    return render_template("combined.html")

if __name__ == "__main__":
    app.run()
