import unittest
from src.data.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()
    
    def test_process_weather_data_empty(self):
        """Test processing empty weather data."""
        result = self.processor.process_weather_data({}, {}, {})
        self.assertEqual(result, {})

if __name__ == "__main__":
    unittest.main()
