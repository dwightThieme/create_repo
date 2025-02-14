# Import the dependencies.
import numpy as np
import datetime as dt
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(autoload_with=engine)

# Save references to each table
measurement = base.classes.measurement
station = base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



# #################################################
# # Flask Routes
# #################################################
@app.route("/")
def homepage():
    """List all available api route"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

# precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    session=Session(engine)

    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precip = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date > year_ago).\
        order_by(measurement.date).all()
    session.close()

    precip = []
    for prcp, date in precip:
        precipitation_dict = {}
        precipitation_dict["precipitation"] = prcp
        precipitation_dict["date"] = date
        precip.append(precipitation_dict)

    return jsonify(dict(precip))

# #stations
@app.route("/api/v1.0/stations")
def stations():
    session=Session(engine)

    station_act = session.query(measurement.station,func.count(measurement.station)).\
        group_by(measurement.station).\
        order_by(func.count(measurement.station).desc()).all()
    session.close()

    station_list = list(np.ravel(station_act))

    return jsonify(station_list)

# # observed temp
@app.route("/api/v1.0/tobs")
def tobs():
    session=Session(engine)

    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    station1_data = session.query(measurement.tobs, measurement.date).\
        filter(measurement.station=='USC00519281', measurement.date >= year_ago).\
        order_by(measurement.tobs).all()
    session.close()

    station1_list = list(np.ravel(station1_data))
    return jsonify(station1_list)

# start
@app.route("/api/v1.0/start")
def temps(start):
    session=Session(engine)

    # start = dt.date(2017, 1, 1)
    start_query = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date >= start).all()
    session.close()

    # start_query = []
    tempobs={}
    tempobs["min"]=start_query[0][0]
    tempobs["max"]=start_query[0][1]
    tempobs["avg"]=start_query[0][2]

    return jsonify(tempobs)

# end
@app.route("/api/v1.0/start/end")
def year_data(start, end):
    session = Session(engine)

    # year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    station1_data = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.station=='USC00519281', measurement.date > start, measurement.date < end).\
        order_by(measurement.tobs).all()

    session.close()

    tempobs={}
    tempobs["min"]=station1_data[0][0]
    tempobs["max"]=station1_data[0][1]
    tempobs["avg"]=station1_data[0][2]
    
    return jsonify(tempobs)

if __name__ == '__main__':
    app.run(debug=True)