import requests
from utils.config import OPENWEATHER_API_KEY, OPENMETEO_API_URL
from utils.logger import setup_logger

class WeatherAPI:
    def __init__(self):
        self.logger = setup_logger()
        self.openweather_base_url = "http://api.openweathermap.org/data/2.5"
        self.openmeteo_base_url = OPENMETEO_API_URL
    
    def get_current_weather(self, lat, lon):
        """Fetch current weather data from OpenWeatherMap."""
        try:
            url = f"{self.openweather_base_url}/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Error fetching current weather: {str(e)}")
            return None

    def get_air_quality(self, lat, lon):
        """Fetch air quality data from OpenWeatherMap."""
        try:
            url = f"{self.openweather_base_url}/air_pollution?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Error fetching air quality: {str(e)}")
            return None

    def get_scientific_metrics(self, lat, lon):
        """Fetch scientific metrics (e.g., UV index, dew point) from Open-Meteo."""
        try:
            url = f"{self.openmeteo_base_url}/forecast?latitude={lat}&longitude={lon}&current=dewpoint_2m,uv_index,pressure_msl"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Error fetching scientific metrics: {str(e)}")
            return None
