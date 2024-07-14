import streamlit as st
import pandas as pd
import requests
import seaborn as sns
import sqlite3
import matplotlib.pyplot as plt

st.title('Taxi Data Explorer')

# Get Table List from API
table_list_response = requests.get('http://127.0.0.1:5010/api/tables')  
table_list = table_list_response.json()  

# Choose Table
if True:
    selected_table = st.selectbox("Select a Table", table_list)

if selected_table:
    # Fetch Data for Selected Table (Corrected URL)
    API_URL = f'http://127.0.0.1:5010/api/data/{selected_table}'  
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error if request is not successful
        taxi_data = pd.DataFrame(response.json())
        st.write("Schema of data",taxi_data.columns.T)
        st.write("Data ",taxi_data)
        st.write('Stats of data',taxi_data.describe())
        st.write("Number of NULL values in data",taxi_data.isna().sum())
        if selected_table=='feb_yellow_tripdata' or selected_table=='march_yellow_tripdata':
            st.write('Total amount',taxi_data['total_amount'].sum())
            st.write('Total Distance covered',taxi_data['trip_distance'].sum())
            st.write('total rows',taxi_data.shape)
        if selected_table=='feb_yellow_tripdata':
            if st.button("Add Trip"):
            
                st.title("New Yellow Trip Data Entry")


                with st.form("trip_data_form"):
                    VendorID = st.number_input("Vendor ID", min_value=1, step=1)
                    tpep_pickup_datetime = st.date_input("Pickup Datetime")
                    tpep_dropoff_datetime = st.date_input("Dropoff Datetime")
                    passenger_count = st.number_input("Passenger Count", min_value=1, step=1)
                    trip_distance = st.number_input("Trip Distance", min_value=0.0, step=0.1)
                    RatecodeID = st.number_input("Ratecode ID", min_value=1, step=1)
                    store_and_fwd_flag = st.text_input("Store and Forward Flag (Y/N)")
                    PULocationID = st.number_input("PULocation ID", min_value=1, step=1)
                    DOLocationID = st.number_input("DOLocation ID", min_value=1, step=1)
                    payment_type = st.number_input("Payment Type (1=Credit Card, 2=Cash, etc.)", min_value=1, step=1)
                    fare_amount = st.number_input("Fare Amount", min_value=0.0, step=0.1)
                    extra = st.number_input("Extra", min_value=0.0, step=0.1)
                    mta_tax = st.number_input("MTA Tax", min_value=0.0, step=0.1)
                    tip_amount = st.number_input("Tip Amount", min_value=0.0, step=0.1)
                    tolls_amount = st.number_input("Tolls Amount", min_value=0.0, step=0.1)
                    improvement_surcharge = st.number_input("Improvement Surcharge", min_value=0.0, step=0.1)
                    total_amount = st.number_input("Total Amount", min_value=0.0, step=0.1)
                    congestion_surcharge = st.number_input("Congestion Surcharge", min_value=0.0, step=0.1)
                    airport_fee = st.text_input("Airport Fee")

                    # Submit button
                    submitted = st.form_submit_button("Submit")
                    if submitted:
                        # Process the data (e.g., send to a Flask API or database)
                        trip_data_add = (
                                 VendorID,
                                 str(tpep_pickup_datetime),  
                                 str(tpep_dropoff_datetime),
                              passenger_count,
                                 trip_distance,
                            RatecodeID,
                               store_and_fwd_flag,
                               PULocationID,
                                 DOLocationID,
                               payment_type,
                            fare_amount,
                                 extra,
                               mta_tax,
                                tip_amount,
                                tolls_amount,
                                improvement_surcharge,
                               total_amount,
                                congestion_surcharge,
                                 airport_fee,
                        )
                        print(trip_data_add)
                        st.write("Data submitted:", trip_data_add)
                        placeholders = ','.join(['?'] * len(taxi_data.columnns))
                        print(placeholders)
                        # Insert data into the table
                        db_name = 'tripdata.db'
                        cursor=sqlite3.connect(db_name)
                        cursor.executemany(f"INSERT INTO {selected_table} VALUES ({placeholders})", trip_data_add)
                            
                        

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data for {selected_table} table: {e}")


else:
    st.error(f"Error fetching data for {selected_table} table from the API")
