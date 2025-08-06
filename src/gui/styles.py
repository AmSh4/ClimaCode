import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def setup_styles():
    """Configure custom styles for the application."""
    style = ttk.Style(theme="flatly")  # Modern theme
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TButton", font=("Helvetica", 10))
    style.configure("TEntry", font=("Helvetica", 10))
    return style
