# Taxi Trips Data Explorer 

>>> This project provides a simple way to explore data using SQL Editor and view taxi trips data web scrapped from 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'. 
**Tech Stack**: Pandas, Numpy, Streamlit, Flask, BeautifulSoup
>> Scrapped data from 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page' website.
>> Once the data is scrapped we have dumped that data into sqlite database.




### Features:
  >>> Flask API:
>  >>    >> Provides endpoints to fetach taxi trip data from SQLITE database i.e, tripdata.db
>  >>    >> Create GET method of feteching all tables data for streamlit
>  >>    >> Created POST method for feb_yellow_tripdata table 
  >>> Streamlit APP:
         >>   Allows you to select which table to explore data
         >>   Display data in a table format. You can also filter data increasing/descreasing order
         >>   You can also add trip data for feb_yellow_tripdata table using form.


>>> The Streamlit app handles API request errors and displays appropiate messages.
