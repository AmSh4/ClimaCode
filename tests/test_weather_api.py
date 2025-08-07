import unittest
from src.api.weather_api import WeatherAPI

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.weather_api = WeatherAPI()
    
    def test_get_current_weather_invalid(self):
        """Test weather API with invalid coordinates."""
        result = self.weather_api.get_current_weather(999, 999)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
