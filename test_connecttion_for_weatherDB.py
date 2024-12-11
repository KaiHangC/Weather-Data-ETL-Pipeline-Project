import pyodbc

# Connection parameters
server = 'DESKTOP-50RFRNU\SQLEXPRESS'  # Replace with your SQL Server instance name or IP address
database = 'WeatherDB'  # Replace with your database name

# Try to establish a connection using Windows Authentication
def test_connection():
    try:
        # Using Windows Authentication (Trusted Connection)
        connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                                    f'SERVER={server};'
                                    f'DATABASE={database};'
                                    f'Trusted_Connection=yes;')
        print("Connection successful!")
        connection.close()
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")

if __name__ == "__main__":
    test_connection()