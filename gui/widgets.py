import tkinter as tk
from tkinter import filedialog

from gui import styles


class BrowseButton(tk.Button):
    def __init__(self, master, font_style=styles.button_font):
        super().__init__(
            master,
            text="Browse",
            font=font_style,
            command=self.on_click
        )
        self.initial_dir = None
        self.callback_func = None

    def on_click(self):
        selected_directory = filedialog.askdirectory(initialdir=self.initial_dir)
        if self.callback_func:
            self.callback_func(selected_directory)


class Button(tk.Button):
    def __init__(self, master, text, font_style=styles.button_font):
        super().__init__(
            master,
            text=text,
            font=font_style,
            command=self.on_click
        )
        self.callback_func = None

    def on_click(self):
        if self.callback_func:
            self.callback_func()


class Label(tk.Label):
    def __init__(self, master, text, font=styles.label_font):
        super().__init__(
            master,
            text=text,
            font=font
        )


class TextBox(tk.Entry):
    def __init__(self, master, width=20, font=styles.textbox_font):
        super().__init__(
            master,
            width=width,
            font=font
        )
