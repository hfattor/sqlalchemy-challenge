import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect database
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

#################################################
# Flask Routes

# Homepage
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<br/>"
        f"(use format YYYY-MM-DD to query minimum, maximum, and average temperature data from a start date forward, "
        f"or use format YYYY-MM-DD/YY-MM-DD to query minimum, maximum, and average temperature data within a date range.)"
    )

# Precipitation data
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation analysis from the most recent 12 months of data available"""
    # Query DB
    results = session.query(Measurement).with_entities(
        Measurement.date, 
        sqlalchemy.func.sum(Measurement.prcp)
        ).filter(Measurement.date >= '2016-08-23').group_by(Measurement.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation data
    prcp_data = []
    for date, prcp in results:
        prcp_date = {}
        prcp_date["date"] = date
        prcp_date["precipitation"] = prcp
        prcp_data.append(prcp_date)

    return jsonify(prcp_data)

# Station list
@app.route("/api/v1.0/stations")
def stations():
    # Create session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all stations
    results = session.query(Station.station, Station.name).all()

    session.close()

    # Create a dictionary from the row data and append to a list of stations
    station_data = []
    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["station name"] = name
        station_data.append(station_dict)

    return jsonify(station_data)

# Temperature observations
@app.route("/api/v1.0/tobs")
def temperature():
    # Create session (link) from Python to the DB
    session = Session(engine)

    """Return a list of temperatures from the most recent 12 months of data 
    available from the most active station measuring this data"""
    # Query temperatures
    results = session.query(Measurement).with_entities(
        Measurement.date, 
        Measurement.tobs
    ).filter(Measurement.station.like('USC00519281')).filter(Measurement.date >= '2016-08-23').group_by(Measurement.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of stations
    temp_data = []
    for date, tobs in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["temp"] = tobs
        temp_data.append(temp_dict)

    return jsonify(temp_data)

# JSON from start date
@app.route("/api/v1.0/<start>")
def startdate(start):
    # Create session (link) from Python to the DB
    session = Session(engine)

    """Fetch the minimum, maximum, and average temperatures for all the dates 
    greater than or equal to the start date supplied by the user, or a 404 if not."""

     results = session.query(Measurement).with_entities(
        Measurement.date, 
        Measurement.tobs
        ).filter(Measurement.date >= {start}).group_by(Measurement.date).all()
        
    session.close()

    # Create a dictionary from the row data and append to a list of temperature data
    start_data = []
    for date, tobs in results:
        start_dict = {}
        start_dict["date"] = date
        start_dict["temp"] = tobs
        start_data.append(start_dict)

    return jsonify(start_data)

if __name__ == '__main__':
    app.run(debug=True)
