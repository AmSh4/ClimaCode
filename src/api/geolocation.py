import geocoder
from utils.logger import setup_logger

class Geolocation:
    def __init__(self):
        self.logger = setup_logger()

    def get_current_location(self):
        """Get current location using IP-based geolocation."""
        try:
            g = geocoder.ip('me')
            if g.ok:
                return g.latlng, g.city, g.country
            else:
                self.logger.error("Geolocation failed")
                return None, None, None
        except Exception as e:
            self.logger.error(f"Geolocation error: {str(e)}")
            return None, None, None

    def get_coordinates(self, city, country):
        """Get coordinates for a given city and country."""
        try:
            query = f"{city}, {country}" if country else city
            g = geocoder.osm(query)
            if g.ok:
                return g.latlng
            else:
                self.logger.error(f"Could not geocode {query}")
                return None
        except Exception as e:
            self.logger.error(f"Geocoding error: {str(e)}")
            return None
