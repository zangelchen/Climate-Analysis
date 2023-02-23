# Climate-Analysis

To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data and plot it in a bar chart. 

![image](https://user-images.githubusercontent.com/117549284/221025614-0f2d4116-4bbf-43c7-8cbf-01c97f382771.png)


Design a query to calculate the total number of stations in the dataset, the most-active stations, and the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query. Then plot into a histogram.

![image](https://user-images.githubusercontent.com/117549284/221025740-d6f2e783-a0f0-4a2c-b7cb-596f4c8e2fcc.png)



Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

/

Start at the homepage and list all the available routes.
![image](https://user-images.githubusercontent.com/117549284/221025010-e881254c-d3e8-46e9-9568-c46462fd7413.png)

/api/v1.0/precipitation
Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.Return the JSON representation of your dictionary.

![image](https://user-images.githubusercontent.com/117549284/221025051-f1304d00-4d61-40bf-b0ea-0c23997a290d.png)

/api/v1.0/stations
Return a JSON list of stations from the dataset.
![image](https://user-images.githubusercontent.com/117549284/221025300-09576f85-8c10-4941-a6cf-1dcf65ed0c08.png)


/api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.Return a JSON list of temperature observations for the previous year.
![image](https://user-images.githubusercontent.com/117549284/221025319-e3ffd8f0-86cf-4c69-86df-a9ea1f2d2dd9.png)

/api/v1.0/<start>  
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
![image](https://user-images.githubusercontent.com/117549284/221025349-fb1e77d2-6399-4ce3-9c58-569173fceff1.png)

/api/v1.0/<start>/<end>
For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
![image](https://user-images.githubusercontent.com/117549284/221025375-e0a06aad-2c24-49fb-8af1-fa439e9124c0.png)

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
