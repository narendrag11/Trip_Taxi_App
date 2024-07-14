# Taxi Trips Data Explorer 

This project provides a simple way to explore data using SQL Editor and view taxi trips data web scrapped from 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'.
 
**Tech Stack** : Pandas, Numpy, Streamlit, Flask, BeautifulSoup, Sqlite4

-> Scrapped data from 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page' website.

-> Once the data is scrapped we have dumped that data into sqlite database (tripdata.db).


### Features:
 **Flask API:**
1. Provides endpoints to fetach taxi trip data from SQLITE database i.e, tripdata.db
2. Create GET method of feteching all tables data 
3. Created POST method for feb_yellow_tripdata table
   
**URL:** : http://127.0.0.1:5010/api/tables this will fetch list of tables present in my tripdata.db database.

**URL** : http://127.0.0.1:5010/api/data/<table_name> will fetch top 10 records of data present in a particular table in my tripdata.db database.


**Streamlit APP:**

for streamlit **BASE URL** : http://localhost:8503
1. Allows you to select which table to explore data
2. Display data in a table format. You can also filter data increasing/descreasing order
3. You can also add trip data for feb_yellow_tripdata table using form.



The Streamlit app handles API request errors and displays appropiate messages.
