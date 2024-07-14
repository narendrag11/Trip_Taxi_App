## System Design

**Component and Interactions**
1. Web Scrapper:
   - Fetches HTML code using python script from target website
   - Parses the HTML to extract desired data fields using beautifulsoup.
   - Cleans and transforms the data for consistency.
   - Store the processed data into the sqlite database.
3. SQLite database:
   - Designed with tables that match the scraped data structure.
   - automatically send the data from dataframe to db using python code.

4. Flask API:
   - Exposes endpoints for:
       - Retrieving data
       - Post, Delete and Update data (yet to do)

5. Streamlit App:
   - Connects to the flask API to fetch data.
   - Uses Streamlit's UI elements to present data.
   - Allows users to interact with the data like sort.


**Scalability Considerations:**

 1. database:
    - For larger dataset, consider migrating to a more robust database like postgresSQL or Oracle or MySQL
    - Implement caching (redis) to reduce database load for frequently accessed data.
 2. Flask API:
    - Use a production ready WSGI server to handle concurrent requests
    - Horizantally scale by deploying multiple API instances behind a load balanacer (using cloud)
   
 3. Streamlit APP:
    - consider using a tast queue like celery for long running data processing tasks.
    - For high traffic, explore streamlit cloud or deploy on a dedicated server.


**Deployement Options:**

1. Local - for developement and testing, run everything on your local machine.
2. Cloud -
     - Deploy the flask API on a cloud platform like GCP, AWS, or Azure
     - Host the streamlit app on a VM/EC2 or streamlit cloud.
     - Use a managed database service like AWS RDS or CloudSQL for easier maintenance.

3. Docker - containerize each componennt for easier deployment and portability.

**Additional feactures:**

1. Logging: Track web scrapper activity, API request and user interactions.
2. Monitoring : set up alerts for scraper failures, API errors and database issues.
3. Error Handling: Implement robust error handling in the scraper, API
