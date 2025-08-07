# ClimaCode

Climacode is a Python 3 desktop application that provides real-time weather data and scientific metrics for any location worldwide. Users can manually enter a city and country or use geolocation to fetch weather details, including temperature, humidity, wind speed, air quality index (AQI), dew point, UV index, and mean sea level pressure. 

The application features a modern graphical user interface (GUI) built with Tkinter and ttkbootstrap, data visualization with Matplotlib, and robust error handling. It integrates the OpenWeatherMap API for standard weather data and the Open-Meteo API for advanced scientific metrics, making it a comprehensive tool for weather enthusiasts and professionals.  
## Folder Structure   
     
      Weather-App/
      │
      ├── src/
      │   ├── __init__.py
      │   ├── main.py
      │   ├── api/
      │   │   ├── __init__.py
      │   │   ├── weather_api.py
      │   │   ├── geolocation.py
      │   ├── gui/
      │   │   ├── __init__.py
      │   │   ├── main_window.py
      │   │   ├── styles.py
      │   ├── data/
      │   │   ├── __init__.py
      │   │   ├── data_processor.py
      │   │   ├── visualizer.py
      │   ├── utils/
      │   │   ├── __init__.p 
      │   │   ├── config.py
      │   │   ├── logger.py
      │   ├── assets/
      │   │   ├── weather_icons/
      │   │   │   ├── clear.png
      │   │   │   ├── clouds.png
      │   │   │   ├── rain.png
      │   │   │   ├── snow.png
      │   │   │   ├── thunderstorm.png
      │   │   │   ├── mist.png
      │
      ├── data/
      │   ├── sample_weather_data.json
      │   ├── historical_weather_data.csv
      │
      ├── tests/
      │   ├── __init__.py
      │   ├── test_weather_api.py
      │   ├── test_data_processor.py
      │
      ├── requirements.txt
      ├── README.md
      ├── LICENSE
      └── .gitignore
## Features
- **Real-Time Weather Data**: Fetches current weather conditions, including temperature, humidity, wind speed, and weather description.
- **Scientific Metrics**: Displays dew point, UV index, and mean sea level pressure, providing insights beyond standard weather apps.
- **Geolocation Support**: Automatically detects the user's location or allows manual input of city and country.
- **Data Visualization**: Plots historical temperature trends using Matplotlib for data analysis.
- **Modern GUI**: Styled with ttkbootstrap for a professional and user-friendly interface.
- **Error Handling**: Robust handling of API failures, invalid inputs, and geolocation errors.
- **Logging**: Maintains detailed logs for debugging and monitoring.
- **Offline Data**: Includes sample datasets for testing and development.

## Installation
1. **Clone the Repository**:  
      Git clone
   ```
      https://github.com/your-username/ClimaCode.git
      cd ClimaCode
3. **Install Dependencies**:
 - Ensure Python 3.8+ is installed.
 - Then, install required packages:
        pip install -r requirements.txt
3. **Obtain API Keys**:
   - Sign up at *OpenWeatherMap* to get an API key.
   - Update src/utils/config.py with your OpenWeatherMap API key:
     ```
       OPENWEATHER_API_KEY = "your-api-key-here"
4. **Run the Application**: 
     ```
       python src/main.py
## Usage
- Manual Location Input: Enter a city and optional country in the GUI, then click "Get Weather" to fetch data.
- Current Location: Click "Use Current Location" to automatically detect and display weather for your location.
- Weather Display: View detailed weather information, including scientific metrics like AQI, dew point, and UV index.
- Visualization: Historical temperature trends are plotted in the "Weather Trends" section.
## Project Structure
- *src/*: Source code directory.
- *main.py*: Entry point for the application.
- *api/*: Modules for API interactions (weather data and geolocation).
- *gui/*: GUI components and styling.
- *data/*: Data processing and visualization modules.
- *utils/*: Configuration and logging utilities.
- *assets/*: Weather icon images.
- *data/*: Sample weather data and historical datasets.
- *tests/*: Unit tests for API and data processing.
- *requirements.txt*: Python dependencies.
- *LICENSE*: MIT License for open-source usage.
- *.gitignore*: Ignores logs, virtual environments, and temporary files.
## Dependencies
- **Python 3.8+**
- **requests**: For API calls
- **geocoder**: For location detection
- **ttkbootstrap**: For GUI styling
- **matplotlib**: For data visualization
## Testing
Run unit tests to verify functionality:
python -m unittest discover tests
## Contributing
- Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.
- Ensure code follows PEP 8 guidelines and includes appropriate tests.
## License
This project is licensed under the MIT License. See the LICENSE file for details.
## Contact
For questions or feedback, please open an issue on the GitHub repository.
