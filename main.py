import tkinter as tk
from tkinter import PhotoImage, messagebox
from data_manager import DataManager
from personal_wiki import PersonalWiki

import os

# This creates an instance of your PersonalWiki class
wiki = PersonalWiki()

# This creates a DataManager instance and pass the wiki and root attributes
user_home = os.path.expanduser("~")
root = tk.Tk()
root.title("Personal Writing Wiki")
root.geometry("1200x720")
root.resizable(False, False)

# Load the background image from the directory
# The image can be either a .gif, .png, or .jpeg. The only issue with .gif is that it won't actually move.
# So if you use a .gif you're only going to have the first frame working. Haven't spent enough time to fix it, was more
# concerned about just getting a regular image to work.
bg_image = tk.PhotoImage(file="/home/lincoln/PycharmProjects/LHallFinalProject/Images/WALLPAPER")

# Creates a label widget to display the background image
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Instantiate the DataManager
data_manager = DataManager(wiki, root)
# Font for the buttons, I just went with TNR for the simplicity, but you can upload custom fonts if you want to
button_font = ("Times New Roman", 20)
button_padding = 44
# Buttons
add_button = tk.Button(root, text="Add Entry", command=data_manager.add_entry_window, font=button_font)
add_button.pack(pady=button_padding)

open_project_button = tk.Button(root, text="Open Project Folder", command=data_manager.open_project, font=button_font)
open_project_button.pack(pady=button_padding)

new_project_button = tk.Button(root, text="New Project Folder", command=data_manager.new_project, font=button_font)
new_project_button.pack(pady=button_padding)

open_folder_entries_button = tk.Button(root, text="Open Folder Entries", command=data_manager.open_folder_entries, font=button_font)
open_folder_entries_button.pack(pady=button_padding)

root.mainloop()
