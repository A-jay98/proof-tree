import tkinter as tk
from .directory_scanner import DirectoryScanner
from gui.menu import get_menu_bar


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Proof Tree")
        self.geometry("500x200")
        self.resizable(True, True)
        # Configure grid for root window
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # add menu to the root window
        menu_bar = get_menu_bar(self)
        self.config(menu=menu_bar)
        directory_scanner = DirectoryScanner(self)
        self.show_frame(directory_scanner.frame)

    def show_frame(self, frame):
        # remove current frame and show new frame
        current_frame = self.winfo_children()[0]
        current_frame.grid_remove()
        frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def switch_frame(self, frame):
        # remove current frame and show new frame
        self.show_frame(frame)

    def run(self):
        self.mainloop()
