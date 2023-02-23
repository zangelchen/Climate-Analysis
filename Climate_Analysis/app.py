import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine,reflect=True)

# Save reference to the table
measurements = Base.classes.measurement
stations = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the SQL-Alchemy APP API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>")


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipating over the past 12 months"""
    # Query all precipitation
    last_date=session.query(measurements.date).order_by(measurements.date.desc()).first()
    one_year_less=last_date[0]
    
    precipitation_results=session.query(measurements.date,measurements.prcp).filter(measurements.date>=one_year_less).all()

    session.close()
    
    # Convert into dictionary

    all_prcpt=[]
    for date, prcp in precipitation_results:
        prcp_dict={}
        prcp_dict["date"]= date
        prcp_dict["prcp"]= prcp
        all_prcpt.append(prcp_dict)

    return jsonify(all_prcpt)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all available stations"""
    # Query all precipitation
    station_results=session.query(stations.station).order_by(stations.station).all()
    
    session.close()
   
    # Convert list of tuples into normal list
    all_station=list(np.ravel(station_results))

    return jsonify(all_station)

@app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all available stations"""
    # Query all dates and temperatures of the most active station by station year
    station_list=session.query(measurements.station,func.count(measurements.station)).group_by(measurements.station)
    sorted_list=station_list.order_by(func.count(measurements.station).desc()).all()
    most_active_station=sorted_list[0][0]

    tobs_results=session.query(measurements.prcp,measurements.date,measurements.tobs).filter(measurements.date>="2016-08-23").filter(measurement.station==most_active_station).all()
    
    session.close()
   
    # Convert into dictionary
    all_tobs=[]
    for prcp, date,tobs in tobs_results:
        tobs_dict={}
        tobs_dict["prco"]= prcp
        tobs_dict["date"]= date
        tobs_dict["tobs"]= tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)


@app.route("/api/v1.0/<start_date>")
def start(start_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return min, avg, max for all tobs at start date """
    # Query all statistics
    start_results=[func.min(measurements.tobs),func.avg(measurements.tobs),func.max(measurements.tobs)]
    #filter(measurements.date>=start_date).all()
    print(start_results)
    session.close()
   
    # Convert into dictionary
    all_start_dates=[]
    for min, avg, max in start_results:
       start_dict={}
       start_dict["min"]= min
       start_dict["avg"]= avg
       start_dict["max"]= max
       all_start_dates.append(start_dict)

   # return jsonify(all_start_dates)


@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end(start_date,end_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return min, max, avg for all tobs at start date """
    # Query all precipitation
    start_end_tobs=session.query(func.min(measurements.tobs),func.avg(measurements.tobs),func.max(measurements.tobs)).\
                           filter(measurements.date>=start_date).filter(measurements.date<=end_date).all()
    
    session.close()
   
    # Convert into dictionary
    all_start_end=[]
    for min, max,avg in start_end_tobs:
        start_end_dict={}
        start_end_dict["min"]= min
        start_end_dict["max"]= max
        start_end_dict["avg"]= avg
        all_start_end.append(start_end_dict)

    return jsonify(all_start_end)

if __name__ == '__main__':
   app.run(debug=True)
