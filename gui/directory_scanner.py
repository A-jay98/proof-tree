import gui
from conf import settings
from .widgets import BrowseButton, Button, Label, TextBox
from .list_window import ListWindow
import tkinter as tk

import os


class DirectoryScanner:
    def __init__(self, parent_window: 'gui.app.App', selected_directory: str = None):
        self.parent_window = parent_window
        if selected_directory:
            self.selected_directory = selected_directory
        elif settings.IO and (sd := settings.IO.get("root", None)):
            self.selected_directory = sd
        else:
            self.selected_directory = os.getcwd()

        # Create Frame
        self.frame = DirectoryPathFrame(self.parent_window)
        # Setup
        self.setup()

    def setup(self):
        # setting callbacks
        self.frame.browse_btn.callback_func = self.set_selected_directory
        self.frame.scan_btn.callback_func = self.scan_directory
        self.set_selected_directory(self.selected_directory)

    def scan_directory(self):
        list_window = ListWindow(self.parent_window, self.selected_directory)
        self.parent_window.switch_frame(list_window.frame)

    def set_selected_directory(self, text):
        self.selected_directory = text
        self.frame.path_textbox.delete(0, tk.END)
        self.frame.path_textbox.insert(0, text)
        self.frame.browse_btn.initial_dir = self.selected_directory
        self.frame.path_textbox.focus()


class DirectoryPathFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.parent_window = master

        label = Label(self, text="Directory Path")
        label.grid(row=0, column=1, sticky="ew")

        self.path_textbox = TextBox(self, width=50)
        self.path_textbox.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.browse_btn = BrowseButton(self)
        self.browse_btn.grid(row=1, column=2)

        self.scan_btn = Button(self, "Scan")
        self.scan_btn.grid(row=2, column=1, sticky="ew")

        for row_num in range(self.grid_size()[0]):
            self.rowconfigure(row_num, weight=1)
        for col_num in range(self.grid_size()[1]):
            self.columnconfigure(col_num, weight=1)
