from flask import Flask, render_template
import altair as alt
import pandas as pd

from models import db, migrate, Car


# create the Flask app
app = Flask(__name__)
app.config.from_object("config.Config")

# initialize plugins
db.init_app(app)
migrate.init_app(app, db)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/data")
def data():
    cars_list = [
        dict(
            name=x.name,
            miles_per_gallon=x.miles_per_gallon,
            horsepower=x.horsepower,
            origin=x.origin,
        )
        for x in Car.query.all()
    ]
    