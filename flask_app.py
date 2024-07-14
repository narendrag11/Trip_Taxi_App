import sqlite3
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Database Helper Functions
def get_db_connection():
    conn = sqlite3.connect('tripdata.db')
    conn.row_factory = sqlite3.Row
    return conn

# Error Handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error.description)}), 400



@app.route('/api/tables', methods=['GET'])
def get_table_list():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query to fetch table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    conn.close()
    return jsonify(tables)

# API Endpoint to Get Data by Table Name
@app.route('/api/data/<table_name>', methods=['GET'])
def get_table_data(table_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    print(table_name)

    try:
        # Fetch limited rows to avoid large responses
        cursor.execute(f'SELECT * FROM {table_name}')  
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        abort(500, description=f"Error querying database: {e}")
    finally:
        conn.close()

    return jsonify([dict(row) for row in rows])


# @app.route('/api/data/<table_name>',method=['POST'])
# def add_data(table_name):
#     if table_name=='feb_yellow_tripdata':
#         trip_data = request.get_json()
#         # mandatory 
#         required_keys = ["VendorID", "tpep_pickup_datetime", "tpep_dropoff_datetime"]
#         if not all(key in trip_data for key in required_keys):
#             return jsonify({"error": "Missing required fields"}), 400

if __name__ == '__main__':
    app.run(debug=True,port=5010)
