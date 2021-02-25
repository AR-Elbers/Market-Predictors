from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

# change to name of your database; add path if necessary
db_name = 'predictions.sqlite'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.schema import MetaData
import pandas as pd
import json

from flask import Flask, jsonify, render_template

engine = create_engine("sqlite:///predictions.sqlite")
conn = engine.connect()

data = engine.execute('SELECT * FROM "returns_actual"').fetchall()
# NOTHING BELOW THIS LINE NEEDS TO CHANGE

@app.route("/api/v1.0/ReturnAct")
def returnact():
    # Create our session (link) from Python to the DB
    # engine = create_engine("sqlite:///predictions.sqlite")
    # conn = engine.connect()
    # data = pd.read_sql("""Select * From return_act""", conn)
    data_json = json.loads(data)


    return jsonify(data_json)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br>"
        f"/api/v1.0/ReturnAct<br/>"
        f"/api/v1.0/ReturnPre<br>"
        f"/api/v1.0/VolatilityAct<br/>"
        f"/api/v1.0/VolatilityPre<br>"
        f"/api/v1.0/HistoricData<br/>"
    )


if __name__ == '__main__':
    app.run(debug=True)