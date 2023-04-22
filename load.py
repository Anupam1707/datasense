from tkinter import *
from tkinter import ttk

load = Tk()

message_label = Label(load, text="Loading, please wait...")
message_label.pack(pady=10)

progress_bar = ttk.Progressbar(load, length=300, mode='indeterminate')
progress_bar.pack(pady=10)

progress_bar.start()

load.title("Loading")
load.mainloop()
