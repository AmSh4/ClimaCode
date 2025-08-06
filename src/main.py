import tkinter as tk
from gui.main_window import WeatherApp
from utils.logger import setup_logger

def main():
    # Initialize logger
    logger = setup_logger()
    logger.info("Starting Weather-App")
    
    try:
        # Initialize and run the application
        root = tk.Tk()
        app = WeatherApp(root)
        root.mainloop()
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
