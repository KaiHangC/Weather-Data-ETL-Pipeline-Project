Weather Data ETL Pipeline
This project implements an ETL (Extract, Transform, Load) pipeline to fetch real-time weather data from the OpenWeatherMap API. The pipeline extracts key weather information such as temperature, humidity, and weather description, processes it, and loads it into a Microsoft SQL Server database for storage and analysis.

Features
Fetches real-time weather data based on latitude and longitude using the OpenWeatherMap API.
Extracts weather data including temperature, humidity, and description.
Transforms the data (e.g., converts Unix timestamps to datetime format).
Loads the processed data into a Microsoft SQL Server database.
Handles errors gracefully and ensures data integrity.
Prerequisites
Python 3.x
Microsoft SQL Server (SSMS)
An OpenWeatherMap API key (you can get it from here)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/weather-data-etl-pipeline.git
cd weather-data-etl-pipeline
Set up a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
.\venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install required Python packages:

bash
Copy code
pip install -r requirements.txt
Configure your SQL Server database connection in the config.py file (e.g., server, database, username, password).

Set up your OpenWeatherMap API key in the config.py file.

Usage
Run the weather_etl.py script to fetch and load weather data:

bash
Copy code
python weather_etl.py
The script will fetch the weather data, transform it, and load it into your SQL Server database.

Files
weather_etl.py: Main script that fetches data from the OpenWeatherMap API and inserts it into SQL Server.
config.py: Configuration file for setting up database credentials and API key.
requirements.txt: List of dependencies for the project.
Troubleshooting
Ensure that your API key is valid and has permissions to access the OpenWeatherMap API.
Make sure your SQL Server instance is running and accessible.
If you're using Windows Authentication for SQL Server, verify that the connection string is correct.
