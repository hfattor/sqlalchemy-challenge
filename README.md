# sqlalchemy-challenge

## Climate Analysis in SQLAlchemy

### Precipitation Analysis

A year of Hawaii precipitation data (from 2016-08-23 to 2017-08-23) is modeled in climate-analysis.ipynb. The bar graph summarizing this data is printed in the output folder as bar1.png.

### Station Analysis

A year of Hawaii temperature data (from 2016-08-23 to 2017-08-23) is modeled in climate-analysis.ipynb. This data was from the weather station with the most data. The histogram summarizing this data is printed in the output folder as hist1.png.

## API Access in Flask
Queries are available through an API interface established by running the app.py file in the computer's command terminal using python. The API homepage lists available routes:

<ul>
    <li>/api/v1.0/precipitation - retrieves preciptiation analysis as outlined above in a JSON format.</li>
    <li>/api/v1.0/stations - returns a JSON list of stations from the dataset.</li>
    <li>/api/v1.0/tobs - returns the temperature observations of the most-active station for the previous year of data in a JSON format.</li>
    <li>/api/v1.0/<em>start_date</em> - returns a JSON list of the minimum, maximum, and average temperature from the date entered (using format YYYY-MM-DD) to the end of the dataset.</li>
    <li>/api/v1.0/<em>start_date</em>/<em>end_date</em> - returns a JSON list of the minimum, maximum, and average temperature from the start date entered (using format YYYY-MM-DD) to the end date entered (using format YYYY-MM-DD).</li>
</ul>
