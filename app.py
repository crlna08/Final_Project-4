from flask import Flask, render_template

import pandas as pd
# From initdb import create_collection

#################################################
# Flask Setup
#################################################
# Instantiate a Flask object at __name__, and save it to a variable called app
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
# index route
@app.route("/")
def index():
    return render_template("index.html")

# tiktok analysis page 
@app.route("/tiktok")
def tiktok():
    return render_template("tiktok.html")

# spotify analysis page 
@app.route("/spotify")
def spotify():
    return render_template("spotify.html")

# tiktok analysis page 
@app.route("/comparison")
def comparison():
    return render_template("comparison.html")

if __name__ == "__main__":
    app.run()
