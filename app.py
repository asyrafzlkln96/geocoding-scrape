from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/subway_locations', methods=['GET'])
def get_subway_locations():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('subway_locations.db')
        cursor = conn.cursor()

        # Pagination parameters
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        # Retrieve data from the database with pagination
        cursor.execute('SELECT name, address, opening_hours, waze_url, latitudes, longitudes FROM subway_locations LIMIT ? OFFSET ?', (per_page, (page - 1) * per_page))
        data = cursor.fetchall()

        # Close the database connection
        conn.close()

        geojson_features = []
        for row in data:
            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [float(row[5]), float(row[4])]
                },
                'properties': {
                    'name': row[0],
                    'address': row[1],
                    'opening_hours': row[2],
                    'waze_url': row[3]
                }
            }
            geojson_features.append(feature)

        geojson = {
            'type': 'FeatureCollection',
            'features': geojson_features
        }

        # Return the GeoJSON data
        return jsonify(geojson)
    except Exception as e:
        # Handle exceptions and return a 500 error
        return jsonify({'Error': str(e), 'Status Code': 500}), 500


@app.route('/map', methods=['GET'])
def show_map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
