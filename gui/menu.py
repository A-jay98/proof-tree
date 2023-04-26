import tkinter as tk

from sys import platform

menu_bar = None

# Check if we're on OS X and fix menu title.
# https://stackoverflow.com/questions/30009909/change-title-of-tkinter-application-in-os-x-menu-bar
if platform == 'darwin':
    from Foundation import NSBundle
    bundle = NSBundle.mainBundle()
    if bundle:
        info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
        if info and info['CFBundleName'] == 'Python':
            info['CFBundleName'] = "Proof Tree"


def save_current_config():
    # Do something to save the current config
    pass


def get_menu_bar(window=None):
    global menu_bar
    if menu_bar:
        return menu_bar
    if not window:
        raise ValueError("Window must be provided to get the menu bar")
    menu_bar = tk.Menu(window)
    file_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save Current Config", command=save_current_config)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit)
    return menu_bar
