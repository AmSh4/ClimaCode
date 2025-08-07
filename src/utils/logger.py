import logging
import os

def setup_logger():
    """Configure logging for the application."""
    logger = logging.getLogger("WeatherApp")
    logger.setLevel(logging.INFO)
    
    # Create logs directory if it doesn't exist
    log_dir = os.path.join(os.path.dirname(__file__), "../../logs")
    os.makedirs(log_dir, exist_ok=True)
    
    # File handler
    file_handler = logging.FileHandler(os.path.join(log_dir, "weather_app.log"))
    file_handler.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
