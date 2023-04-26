import tkinter as tk

import gui
import gui.styles as styles
from .widgets import Button
from utils import list_tex_files


class ListWindow:
    def __init__(self, parent_window: 'gui.app.App', directory_path: str):
        self.parent_window = parent_window
        self.directory_path = directory_path
        self.files_list = list_tex_files(self.directory_path)

        # Create Frame
        self.frame = ListWindowFrame(self.parent_window)

        # Setup
        self.setup()

    def setup(self):
        self.parent_window.title(f"List of Tex files in {self.directory_path}")

        for filename in self.files_list:
            self.frame.listbox.insert(tk.END, filename)
        self.frame.listbox.focus()
        self.frame.listbox.bind("<Double-Button-1>", self.on_double_click)
        self.frame.back_button.callback_func = self.go_back

    def go_back(self):
        from . import DirectoryScanner
        directory_scanner = DirectoryScanner(self.parent_window, self.directory_path)
        self.parent_window.switch_frame(directory_scanner.frame)

    def on_double_click(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = self.files_list[selection[0]]
        print("selected:", value)


class ListWindowFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.parent_window = master

        self.listbox = tk.Listbox(self, font=styles.listbox_font)
        self.listbox.grid(row=1, column=2, sticky="nsew", rowspan=5)

        self.back_button = Button(self, text="Back")
        self.back_button.grid(row=0, column=0)

        for row_num in range(self.grid_size()[0])[1:]:
            self.rowconfigure(row_num, weight=1)
        for col_num in range(self.grid_size()[1])[1:]:
            self.columnconfigure(col_num, weight=1)