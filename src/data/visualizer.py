import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.logger import setup_logger

class WeatherVisualizer:
    def __init__(self):
        self.logger = setup_logger()
    
    def plot_temperature_trend(self, canvas, historical_data):
        """Plot historical temperature trend on the provided canvas."""
        try:
            plt.clf()  # Clear previous plot
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(historical_data, label="Temperature (°C)", color="blue")
            ax.set_title("Historical Temperature Trend")
            ax.set_xlabel("Time (hours)")
            ax.set_ylabel("Temperature (°C)")
            ax.legend()
            ax.grid(True)
            
            # Embed plot in Tkinter canvas
            for widget in canvas.winfo_children():
                widget.destroy()
            canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
            canvas_agg.draw()
            canvas_agg.get_tk_widget().pack(fill="both", expand=True)
        except Exception as e:
            self.logger.error(f"Error plotting temperature trend: {str(e)}")
