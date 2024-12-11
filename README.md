# Weather Data ETL Pipeline

This project implements an ETL (Extract, Transform, Load) pipeline to fetch real-time weather data from the OpenWeatherMap API. The pipeline extracts key weather information such as temperature, humidity, and weather description, processes it, and loads it into a Microsoft SQL Server database for storage and analysis.

## Features
- Fetches real-time weather data based on latitude and longitude using the OpenWeatherMap API.
- Extracts weather data including temperature, humidity, and description.
- Transforms the data (e.g., converts Unix timestamps to datetime format).
- Loads the processed data into a Microsoft SQL Server database.
- Handles errors gracefully and ensures data integrity.

## Prerequisites
- Python 3.x
- Microsoft SQL Server (SSMS)
- An OpenWeatherMap API key 
