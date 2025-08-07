import json
import os
from utils.logger import setup_logger

class DataProcessor:
    def __init__(self):
        self.logger = setup_logger()
        self.data_dir = os.path.join(os.path.dirname(__file__), "../../data")
        
    def process_weather_data(self, weather_data, air_quality, scientific_data):
        """Process and combine weather data from multiple APIs."""
        try:
            processed = {
                "city": weather_data.get("name", "Unknown"),
                "country": weather_data.get("sys", {}).get("country", "Unknown"),
                "temperature": weather_data.get("main", {}).get("temp", 0),
                "humidity": weather_data.get("main", {}).get("humidity", 0),
                "wind_speed": weather_data.get("wind", {}).get("speed", 0),
                "condition": weather_data.get("weather", [{}])[0].get("description", "N/A"),
                "aqi": air_quality.get("list", [{}])[0].get("main", {}).get("aqi", 0),
                "dew_point": scientific_data.get("current", {}).get("dewpoint_2m", 0),
                "uv_index": scientific_data.get("current", {}).get("uv_index", 0),
                "pressure_msl": scientific_data.get("current", {}).get("pressure_msl", 0),
                "historical_data": self.load_historical_data()
            }
            return processed
        except Exception as e:
            self.logger.error(f"Error processing weather data: {str(e)}")
            return {}

    def load_historical_data(self):
        """Load sample historical data for visualization."""
        try:
            with open(os.path.join(self.data_dir, "historical_weather_data.csv"), "r") as f:
                lines = f.readlines()
                return [float(line.split(",")[1]) for line in lines[1:]]  # Temperature column
        except Exception as e:
            self.logger.error(f"Error loading historical data: {str(e)}")
            return []

    def format_display_text(self, data):
        """Format weather data for display."""
        aqi_levels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}
        return (
            f"Location: {data.get('city', 'N/A')}, {data.get('country', 'N/A')}\n"
            f"Temperature: {data.get('temperature', 0):.1f}°C\n"
            f"Condition: {data.get('condition', 'N/A').capitalize()}\n"
            f"Humidity: {data.get('humidity', 0)}%\n"
            f"Wind Speed: {data.get('wind_speed', 0)} m/s\n"
            f"Air Quality Index: {aqi_levels.get(data.get('aqi', 0), 'N/A')}\n"
            f"Dew Point: {data.get('dew_point', 0):.1f}°C\n"
            f"UV Index: {data.get('uv_index', 0)}\n"
            f"Pressure (MSL): {data.get('pressure_msl', 0)} hPa"
              )
