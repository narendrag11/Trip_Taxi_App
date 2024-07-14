Approach to create Taxi Trips Data Explorer:

- step 1: Web Scrapping
  - Used beautifulSoup to extract data from the target website
  - If the status.code is not equal to 200 we will print that "we can't scrape data from this webiste".
  - Identified the specific element (id='faq2019' since we want 2019 year ) within the website's HTML that contains the data we want to collect all href links within that element.
  - After href links are extracted, we will use slice to sepearate lists for feb and march 2019 data.
  - Pandas are used to read parquet files from extracted links.
  - We have limited to first 1,00,000 records because of memory issues.
  - Created dictionary of month_trips to store the loaded datframes, using their names as keys.
  - Created clean_and_convert_df function to iterate over each column in the dataframe and remove non-ASCII characters if the column is string type and replace any NaN, NaT or None values with "NULL".
  - Created a connection with sqlite database using sqlite3 module.
  - Iterated over each dataframe in the month_trips dictionary and for each dataframe, We have dynamically created a table in the database if it doesn't exists based on the dataframes columns and their data types.
  - Once the schema is defined in database we have converted dataframe data into list of tuples and inserted into table.


- Step 2: Flask API for creating endpoints
  -   Created a get_db_connection() method to connect with sqlite database (tripdata.db)
  -   created @app.errorhandler(400) decorator that registers the bad_request function as the error handler for HTTP 400 bad request error.
  -   @app.errorhandler() will return a json response containing the error description and set HTTP status code as 400.
  -   Designed API endpoint URL /api/tables will return json response of list of tables present in database.
  -   Designed API endpoint URL /api/data/<table_name> will return the json reponse of all the rows present that table.
 

- Step 3: Streamlit App
- Trips Page
  -   Fetched data from the flask api endpoint using requests
  -   Created a fetch_table_list(): function which makes GET api request to api/tables to get list of available tables, it will return python object.
  -   if the fetch_Table_list() request fails, it will show an error message using st.error and return a empty list.
  -   Created a fetch_table_data(table_name), this will take table_name as input and makes a GET api request to /api/table/{table_name} to fetch the data for that table.
  -   If the fetch_table_data(table_name) is successful, it converts the json response into pandas dataframe and st.write(trip_data) will display that data.
  -   If the request is fail, it will show an error messages and return None.

- SQLite Editor Page
  - Defined a fuction execute_query(query,conn) which basically execute the query using pd.read_sql_query which reads the SQL result directly into pandas dataframe.
  - The function also includes error handling like sqlite3.error which catches errors specific to SQLite and pd.io.sql.DatabaseError will catches errors related to pandas sql interactions.
  - The function get_db_conection(db_file=None) will establish the connection to the SQLite database. If the there's a file provided by the user, it will be used. Otherwise it connect to the default database tripdata.db.
  - The main function is the core app logic, using st_ace we can create a code editor where the user can enter their SQL query.
  - If the user toggles the "show DB schema" button, it will executes a query to get the schema information (sqlite_master table) and display it in a dataframe.
  - Similary for " Show tables " will fetches a list of available tables and display them.
  - Finally, if the user clicks on "Execute Query" button, it call the execute_query function to run the SQL query.
  - If the query is successful and returns a result, it display the results in a dataframe.
  - If the query is susccessful but no results are found, it will show an Error or informational messages to users.
  - 
  
