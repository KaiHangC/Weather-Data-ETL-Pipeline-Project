import requests

# Set your OpenWeatherMap API key here
API_KEY = ''

# Coordinates for the location you want weather data for
LAT = 45.133  # Latitude of the location
LON = 7.367  # Longitude of the location

# Construct the API URL
URL = f'http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric'

# Fetch weather data from OpenWeatherMap
def fetch_weather_data():
    try:
        # Send GET request to the OpenWeatherMap API
        response = requests.get(URL)
        
        # Check if the response status code is 200 (OK)
        response.raise_for_status()
        
        # Return the response as JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

# Main function to test the API
def main():
    # Fetch the weather data
    weather_data = fetch_weather_data()
    
    if weather_data:
        print("Successfully fetched weather data!")
        print("Weather data:", weather_data)
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()