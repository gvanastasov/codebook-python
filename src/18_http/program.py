# Chapter 18: Working with APIs (Simulated with Flask in a Single Script)

"""
Introduction:
In this chapter, we will simulate an interaction with an API by setting up a local Flask web service to return mock weather data. The script will both run the Flask web server and send a request to the server to fetch and process the weather data.

Key Concepts:
1. **APIs**: APIs allow different software systems to communicate and exchange data. They expose endpoints where you send requests and get responses.
2. **Simulating API Calls**: We simulate API calls using a local Flask server, which returns mock data when queried.
3. **HTTP Requests and JSON Parsing**: We will use the `requests` library to make HTTP requests and parse the returned JSON data.

Notes:
- The Flask server will run locally in the background while the program fetches data from it.
- This is a great way to practice API requests and responses before interacting with real APIs.

"""

import json  # Importing the json module
import threading  # To run Flask server in the background
from flask import Flask, jsonify
import requests  # For making HTTP requests

# Function to start the Flask server
def start_flask_server():
    app = Flask(__name__)

    @app.route('/weather', methods=['GET'])
    def get_weather():
        # Simulated weather data for demonstration
        fake_weather_data = {
            "name": "London",
            "sys": {
                "country": "GB"
            },
            "main": {
                "temp": 18.3,  # Temperature in Celsius
                "humidity": 70  # Humidity in percentage
            },
            "weather": [{
                "description": "overcast clouds"
            }],
            "wind": {
                "speed": 4.5  # Wind speed in m/s
            }
        }
        return jsonify(fake_weather_data)

    # Run the Flask server on port 5000
    app.run(debug=True, use_reloader=False, port=5000)

# Function to fetch weather data from the local Flask server
def fetch_weather(city):
    """Fetch weather data for a specific city from the local Flask server."""
    
    # Define the local API URL (where Flask is running)
    url = 'http://127.0.0.1:5000/weather'
    
    # Send a GET request to the local Flask server
    try:
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract relevant weather information
            city_name = data['name']
            country = data['sys']['country']
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            # Print the weather information
            print(f"Weather in {city_name}, {country}:")
            print(f"Temperature: {temperature}°C")
            print(f"Weather: {weather_description.capitalize()}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            # If the request was not successful, display an error
            print(f"Error: Unable to fetch weather data. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")

# Main function to simulate both starting the Flask server and making the request
def main():
    # Run the Flask server in a separate thread so that we can make requests while it's running
    flask_thread = threading.Thread(target=start_flask_server)
    flask_thread.daemon = True  # Ensure the Flask server stops when the main program ends
    flask_thread.start()

    # Fetch weather data after a short delay to allow the server to start
    import time
    time.sleep(1)  # Wait for the server to initialize
    city = 'London'  # City to fetch weather for
    fetch_weather(city)

# Start the main program
if __name__ == '__main__':
    main()
