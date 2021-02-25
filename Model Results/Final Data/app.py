import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.schema import MetaData
import pandas as pd
import json

from flask import Flask, jsonify, render_template


#################################################
# Database Setup
#################################################
# engine = create_engine("sqlite:///predictions.sqlite")
# conn = engine.connect()


# meta = MetaData()
# meta.reflect(bind=engine)



engine = create_engine("sqlite:///predictions.sqlite")
conn = engine.connect()

data = pd.read_sql("""select * from return_act""", conn).to_json(orient ='records')
# Save reference to the table
# return_act = engine.execute('SELECT * FROM return_act').fetchall()
# return_pre = meta.tables['ReturnsPre']
# volatility_act = meta.tables['VolatilityAct']
# volatility_pre = meta.tables['VolatilityPre']
# historic_data = meta.tables['HistoricData']
# session = Session(engine)



#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################


@app.route("/api/v1.0/ReturnAct")
def returnact():
    # Create our session (link) from Python to the DB
    # engine = create_engine("sqlite:///predictions.sqlite")
    # conn = engine.connect()
    # data = pd.read_sql("""Select * From return_act""", conn)
    data_json = json.loads(data)

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

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

# @app.route("/index")
# def index():
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
