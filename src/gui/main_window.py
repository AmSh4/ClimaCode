import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from api.weather_api import WeatherAPI
from api.geolocation import Geolocation
from data.data_processor import DataProcessor
from data.visualizer import WeatherVisualizer
from gui.styles import setup_styles
from utils.logger import setup_logger

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather-App")
        self.root.geometry("800x600")
        self.logger = setup_logger()
        self.weather_api = WeatherAPI()
        self.geolocation = Geolocation()
        self.data_processor = DataProcessor()
        self.visualizer = WeatherVisualizer()
        
        # Apply styles
        self.style = setup_styles()
        
        # Initialize GUI components
        self.create_widgets()
        
        # Load initial data
        self.load_current_location_weather()

    def create_widgets(self):
        """Create GUI components."""
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill="both", expand=True)
        
        # Location input
        self.location_frame = ttk.LabelFrame(self.main_frame, text="Location", padding=10)
        self.location_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(self.location_frame, text="City:").grid(row=0, column=0, padx=5, pady=5)
        self.city_entry = ttk.Entry(self.location_frame)
        self.city_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.location_frame, text="Country:").grid(row=0, column=2, padx=5, pady=5)
        self.country_entry = ttk.Entry(self.location_frame)
        self.country_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Button(self.location_frame, text="Get Weather", command=self.get_weather_manual).grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(self.location_frame, text="Use Current Location", command=self.load_current_location_weather).grid(row=0, column=5, padx=5, pady=5)
        
        # Weather display
        self.weather_frame = ttk.LabelFrame(self.main_frame, text="Weather Information", padding=10)
        self.weather_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.weather_label = ttk.Label(self.weather_frame, text="Enter a location to see weather data.", wraplength=700)
        self.weather_label.pack(pady=10)
        
        # Visualization frame
        self.viz_frame = ttk.LabelFrame(self.main_frame, text="Weather Trends", padding=10)
        self.viz_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.canvas = ttk.Canvas(self.viz_frame)
        self.canvas.pack(fill="both", expand=True)

    def get_weather_manual(self):
        """Fetch weather data for manually entered location."""
        city = self.city_entry.get().strip()
        country = self.country_entry.get().strip()
        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return
        
        coordinates = self.geolocation.get_coordinates(city, country)
        if coordinates:
            self.update_weather_display(*coordinates)
        else:
            messagebox.showerror("Error", "Could not find location.")

    def load_current_location_weather(self):
        """Fetch weather data for current location."""
        coordinates, city, country = self.geolocation.get_current_location()
        if coordinates:
            self.city_entry.delete(0, tk.END)
            self.country_entry.delete(0, tk.END)
            self.city_entry.insert(0, city or "")
            self.country_entry.insert(0, country or "")
            self.update_weather_display(*coordinates)
        else:
            messagebox.showerror("Error", "Could not detect current location.")

    def update_weather_display(self, lat, lon):
        """Update the GUI with weather data."""
        try:
            weather_data = self.weather_api.get_current_weather(lat, lon)
            air_quality = self.weather_api.get_air_quality(lat, lon)
            scientific_data = self.weather_api.get_scientific_metrics(lat, lon)
            
            if not all([weather_data, air_quality, scientific_data]):
                messagebox.showerror("Error", "Failed to fetch weather data.")
                return
                
            processed_data = self.data_processor.process_weather_data(weather_data, air_quality, scientific_data)
            display_text = self.data_processor.format_display_text(processed_data)
            
            self.weather_label.config(text=display_text)
            
            # Update visualization
            self.visualizer.plot_temperature_trend(self.canvas, processed_data.get("historical_data", []))
            
        except Exception as e:
            self.logger.error(f"Error updating weather display: {str(e)}")
            messagebox.showerror("Error", "An error occurred while fetching weather data.")
