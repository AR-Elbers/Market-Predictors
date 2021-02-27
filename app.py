import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
# from password import pw
import json


from flask import Flask, jsonify, render_template


path = 'postgresql://postgres:postgres@localhost:5432/rpi_comp'

engine = create_engine(path)
conn = engine.connect()

# Access our DB through pandas dataframe - convert to json - record oriented
return_act = pd.read_sql("SELECT * FROM returns_actual", conn).to_json(orient='records')

return_pre = pd.read_sql("SELECT * FROM returns_prediction", conn).to_json(orient='records')

vol_act = pd.read_sql("SELECT * FROM volatility_actual", conn).to_json(orient='records')

vol_pre = pd.read_sql("SELECT * FROM volatility_prediction", conn).to_json(orient='records')

historic = pd.read_sql("SELECT * FROM historic_data", conn).to_json(orient='records')



# Access database through sql alchemy
# db = engine.execute('SELECT * FROM "rpi"').fetchall()

# Create Session
session = Session(engine)

# Create Flask connection
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/vol_pre")
def vol_p():

# Convert string to json 

    data_json = json.loads(vol_pre)

    return jsonify(data_json)



@app.route("/api/v1.0/return_act")
def ret_a():

# Convert string to json 

    data_json = json.loads(return_act)

    return jsonify(data_json)



@app.route("/api/v1.0/return_pre")
def ret_p():

# Convert string to json 

    data_json = json.loads(return_pre)

    return jsonify(data_json)


@app.route("/api/v1.0/vol_act")
def vol_a():

# Convert string to json 

    data_json = json.loads(vol_act)

    return jsonify(data_json)


@app.route("/api/v1.0/historic")
def hist():

# Convert string to json 

    data_json = json.loads(vol_act)

    return jsonify(data_json)



@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br>"
        f"/api/v1.0/return_act<br/>"
        f"/api/v1.0/return_pre<br/>"
        f"/api/v1.0/vol_act<br/>"
        f"/api/v1.0/vol_pre<br>"
        f"/api/v1.0/historic<br/>"
    )


@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)