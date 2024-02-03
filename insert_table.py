
import sqlite3

conn = sqlite3.connect('subway_locations.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store Subway locations
cursor.execute('''
    CREATE TABLE IF NOT EXISTS subway_locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        address TEXT,
        opening_hours TEXT,
        waze_url TEXT,
        latitudes REAL,
        longitudes REAL
    )
''')


def insert_data(names, addresses, opening_hours_list, waze_urls, latitudes, longitudes):
	# Check if all lists have the same length
	if len(names) != len(addresses) or len(names) != len(opening_hours_list) or len(names) != len(waze_urls):
		print("Error: All lists must have the same length.")

	# Insert the data into the table
	data = zip(names, addresses, opening_hours_list, waze_urls, latitudes, longitudes)
	cursor.executemany('''
        INSERT OR REPLACE INTO subway_locations (name, address, opening_hours, waze_url, latitudes, longitudes)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', data)
	conn.commit()
	# conn.close()
