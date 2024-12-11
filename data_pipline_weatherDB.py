import requests
import pyodbc
import json
import datetime

# Set your OpenWeatherMap API key here
API_KEY = 'eabba9e77e72237291c7a10ee1937237'

# Coordinates for the location you want weather data for
LAT = 45.133  # Latitude of the location
LON = 7.367  # Longitude of the location

# Construct the API URL
URL = f'http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric'

# SQL Server connection details (change according to your setup)
server = 'DESKTOP-50RFRNU\SQLEXPRESS'  # Replace with your SQL Server instance name or IP address
database = 'WeatherDB'  # Replace with your database name

# Establish a connection to SQL Server
def connect_to_sql():
    try:
        # Using Windows Authentication (Trusted Connection)
        connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                                    f'SERVER={server};'
                                    f'DATABASE={database};'
                                    f'Trusted_Connection=yes;')
        print("Connection successful!")
        return connection
    except Exception as e:
        print("Error connecting to SQL Server:", e)
        return None

# Fetch weather data from OpenWeatherMap
def fetch_weather_data():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Check if request was successful
        return response.json()  # Return the response as a JSON object
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None


# Insert weather data into SQL Server
def insert_weather_data(data):
    if data:
        try:
            conn = connect_to_sql()
            if conn:
                cursor = conn.cursor()
                
                # Extract relevant data from the response
                city_name = data['name']
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                weather_description = data['weather'][0]['description']
                dt = datetime.datetime.fromtimestamp(data['dt'])
                timestamp = dt  # Unix timestamp

                # SQL query to insert data
                query = '''INSERT INTO WeatherData (city_name, temperature, humidity, weather_description, timestamp)
                           VALUES (?, ?, ?, ?, ?)'''
                
                # Execute the insert query
                cursor.execute(query, (city_name, temperature, humidity, weather_description, timestamp))
                conn.commit()
                print(f"Weather data for {city_name} inserted successfully!")

        except pyodbc.Error as e:
            print("Error inserting data into SQL Server:", e)
        finally:
            if conn:
                conn.close()



# Main function to orchestrate everything
def main():
    # Fetch weather data
    weather_data = fetch_weather_data()
    
    if weather_data:
        # Insert the fetched weather data into SQL Server
        insert_weather_data(weather_data)

if __name__ == "__main__":
    main()