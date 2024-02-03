from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/subway_locations', methods=['GET'])
def get_subway_locations():
	try:
	    # Connect to the SQLite database
	    conn = sqlite3.connect('selenium-method/subway_locations.db')
	    cursor = conn.cursor()

	    # Retrieve data from the database
	    cursor.execute('SELECT name, address, opening_hours, waze_url, latitudes, longitudes FROM subway_locations')
	    data = cursor.fetchall()

	    # Close the database connection
	    conn.close()

	    # Convert data to JSON format
	    result = []
	    for row in data:
	        result.append({
	            'name': row[0],
	            'address': row[1],
	            'opening_hours': row[2],
	            'waze_url': row[3],
	            'latitudes': row[4],
	            'longitudes': row[5]
	        })

	    # Return the data as JSON
	    return jsonify(result)
	except Exception as e:
	# Handle exceptions and return a 500 error
		return jsonify({'Error': str(e), 'Status Code': 500}), 500

@app.route('/map', methods=['GET'])
def show_map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
