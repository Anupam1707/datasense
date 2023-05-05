from tkinter import *
from PIL import Image, ImageTk
import os
import requests
from tkinter.ttk import Progressbar

# Create the main window
root = Tk()

# Set the window properties
root.overrideredirect(True)  # Removes the title bar and borders
root.wm_attributes("-topmost", True)  # Keep the window on top
root.wm_attributes("-alpha", 0.7)  # Set the window transparency

# Load and display the logo image
logo_image = ImageTk.PhotoImage(Image.open("splash.png"))
logo_label = Label(root, image=logo_image)
logo_label.pack(pady=50)

# Add a loading spinner
spinner_label = Label(root, text="Loading...", font=("Arial", 12))
spinner_label.pack(pady=10)
spinner = Progressbar(root, mode="indeterminate")
spinner.pack(pady=10)
spinner.start()

# Position the window at the center of the screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
x = (width // 2) - (logo_image.width() // 2)
y = (height // 2) - (logo_image.height() // 2)
root.geometry("+{}+{}".format(x, y))

# Create a list of the module URLs to load
module_urls = [
    "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/db.py",
    "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/visuals.py",
    "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/numeric.py",
    "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/window.py"
]

# Load each module
for i, module_url in enumerate(module_urls):
    exec(requests.get(module_url).text)

# Stop the loading spinner
spinner.stop()
spinner_label.destroy()

# Destroy the translucent window
root.destroy()

# Call the function to display the login window after a 1-second delay
root.after(1000, login_window)

# Run the main event loop
mainloop()
