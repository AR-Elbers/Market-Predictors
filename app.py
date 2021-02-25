from sqlalchemy import create_engine, func
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine, autoflush=False)
session = Session()

from sqlalchemy import Column, Integer, String, Sequence
import json
import numpy as np

from flask import Flask

class act_ret_db(Base):
    __tablename__ = 'return_act'

    id = Column(Integer, Sequence("index"), primary_key=True)
    nas_return = Column(Integer)
    nik_return = Column(Integer)
    gold_return = Column(Integer)
    bonds_return = Column(Integer)
    average_return = Column(Integer)
    day_count = Column(Integer)

    def __repr__(self):
        return "<act_ret_db(nas_return='%s', nik_return='%s', gold_return='%s',bonds_return='%s',average_return='%s',day_count='%s')>" % (self.nas_return, self.nik_return, self.gold_return, self.bonds_return, self.average_return, self.day_count)

Base.metadata.create_all(engine)

from sqlalchemy.ext.automap import automap_base

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

actual_returns = Base.classes.predictions

#################################################
# Flask Setup
#################################################
app = Flask(__name__)





@app.route("/api/v1.0/ReturnAct")
def returnact():
    session = Session(engine)
    # Create our session (link) from Python to the DB
    results = session.query(actual_returns).all()
    # Convert list of tuples into normal list
    data_json = json.dumps(results)
    # results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    # session.close()


    return data_json

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
