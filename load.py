from tkinter import *
def load():
    from tkinter import ttk

    def start_loading():

            message_label = Label(load, text="Loading, please wait...")
            message_label.pack(pady=10)

            progress_bar = ttk.Progressbar(load, length=300, mode='indeterminate')
            progress_bar.pack(pady=10)

            progress_bar.start()
             
load = Tk()
load.title("Loading")

start_loading()
load.mainloop()
load()
