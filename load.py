from tkinter import *
def load():
    from tkinter import ttk

    def start_loading():

            message_label = Label(window, text="Loading, please wait...")
            message_label.pack(pady=10)

            progress_bar = ttk.Progressbar(window, length=300, mode='indeterminate')
            progress_bar.pack(pady=10)

            progress_bar.start()
             
    window = Tk()
    window.title("Loading")

    start_loading()
    window.mainloop()
