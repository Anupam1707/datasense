#Food Analysis App Launcher
"""This Program compiles all the tools required by Food Analysis App and launches the Login Page"""

# Import all libraries required by the app here
from io import BytesIO
import os
import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Install libraries if not found
try:
    import requests
    from tkinter import *
    from PIL import Image, ImageTk
    import numpy as np
    import matplotlib.pyplot as plt
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
except ImportError:
    os.system("pip install requests pillow numpy matplotlib gspread oauth2client")

# Define the function that loads and executes the required modules
def call():
    # Create a list of the module URLs to load
    module_urls = [
        "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/db.py",
        "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/visuals.py",
        "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/numeric.py",
        "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/window.py"
    ]

    # Set the maximum progress value based on the number of modules to load
    max_progress = len(module_urls)

    # Initialize the progress value to zero
    progress = 0
    progress_bar.config(maximum=max_progress, value=progress)

    # Load each module and increment the progress value
    for module_url in module_urls:
        exec(requests.get(module_url).text)
        progress += 1
        progress_bar.config(value=progress)
        load.update_idletasks()

    # Stop the progress bar and destroy the window
    progress_bar.stop()
    load.destroy()

    # Call the function to launch the login window
    login_window()

# Create the main window
load = Tk()
load.title("Loading")

# Add a label to show the loading message
message_label = Label(load, text="Loading, please wait...")
message_label.pack(pady=10)

# Add a progress bar to show the loading progress
progress_bar = ttk.Progressbar(load, length=300, mode='determinate')
progress_bar.pack(pady=10)

# Start the progress bar
progress_bar.start()

# Call the function that will stop the progress bar and destroy the window after it has finished executing
load.after(0, call)

# Run the main event loop
load.mainloop()
