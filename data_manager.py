import tkinter as tk
from tkinter import simpledialog, filedialog
from tkinter.messagebox import showinfo, showerror
import os


# Creates a DataManager class to manage the data functions
class DataManager:
    def __init__(self, wiki, root):
        # This will initialize the DataManager with references to the PersonalWiki instance/Tkinter root
        self.wiki = wiki
        self.root = root
        self.user_home = os.path.expanduser("~")  # Define user_home here

    # This is going to create a window for adding a new entry
    def add_entry_window(self):
        def add_entry():
            title = title_entry.get()
            content = content_text.get("1.0", tk.END)
            if not title:
                showerror("Error", "Title cannot be empty!")
            else:
                if self.wiki.project_directory:
                    self.wiki.add_entry(title, content)
                    showinfo("Info", "Entry added successfully!")
                    add_entry_window.destroy()
                else:
                    showerror("Error", "Choose a project folder first!")

        add_entry_window = tk.Toplevel(self.root)
        add_entry_window.title("Add Entry")
        add_entry_window.geometry("900x600")
        title_entry = tk.Entry(add_entry_window)

        title_label = tk.Label(add_entry_window, text="Title:")
        title_label.pack()
        title_entry = tk.Entry(add_entry_window)


        title_entry = tk.Entry(add_entry_window)
        title_entry.pack()

        content_label = tk.Label(add_entry_window, text="Content:")
        content_label.pack()
        title_entry = tk.Entry(add_entry_window)


        content_text = tk.Text(add_entry_window, wrap=tk.WORD, width=40, height=25)
        content_text.pack()

        add_button = tk.Button(add_entry_window, text="Add Entry", command=add_entry)
        add_button.pack()

    def open_project(self):
        # This function opens an existing project folder
        documents_folder = os.path.join(self.user_home, "Documents")
        selected_directory = filedialog.askdirectory(initialdir=documents_folder)
        if selected_directory:
            self.wiki.set_project_directory(selected_directory)
            showinfo("Info", f"Project folder set to '{selected_directory}'")

    def new_project(self):
        # This function is going to create a new project folder
        project_name = simpledialog.askstring("New Project", "Enter the project name:")
        if not project_name:
            showerror("Error", "Project name cannot be empty.")
            return

        documents_folder = os.path.join(self.user_home, "Documents")
        project_directory = os.path.join(documents_folder, project_name)

        if not os.path.exists(project_directory):
            os.makedirs(project_directory)

        self.wiki.set_project_directory(project_directory)
        showinfo("Info", f"New project '{project_name}' created in the Documents folder.")

    def open_folder_entries(self):
        # This is going to open the folder that has entry files/.txt files
        if not self.wiki.project_directory:
            showerror("Error", "Choose a project folder first!")
            return

        entries_directory = os.path.join(self.wiki.project_directory, "entries")

        if not os.path.exists(entries_directory):
            showinfo("Info", "No entry files found in the project folder.")
            return

        entry_files = [f for f in os.listdir(entries_directory) if f.endswith(".txt")]

        if not entry_files:
            showinfo("Info", "No .txt entry files found in the project folder.")
            return

        selected_file = filedialog.askopenfilename(
            initialdir=entries_directory,
            title="Select an entry file to open",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )

        if selected_file:
            with open(selected_file, 'r') as file:
                content = file.read()

            self.edit_entry_window(content)

    def edit_entry_window(self, content):
        # This function creates a window so you can edit an entry
        def edit_entry():
            title = title_entry.get()
            content = content_text.get("1.0", tk.END)
            if not title:
                showerror("Error", "Title cannot be empty.")
            else:
                if self.wiki.project_directory:
                    self.wiki.add_entry(title, content)
                    showinfo("Info", "Entry edited successfully")
                    edit_entry_window.destroy()
                else:
                    showerror("Error", "Choose a project folder first!")

        edit_entry_window = tk.Toplevel(self.root)
        edit_entry_window.title("Edit Entry")
        edit_entry_window.geometry("900x600")

        title_label = tk.Label(edit_entry_window, text="Title:")
        title_label.pack()

        title_entry = tk.Entry(edit_entry_window)
        title_entry.pack()

        content_label = tk.Label(edit_entry_window, text="Content:")
        content_label.pack()

        content_text = tk.Text(edit_entry_window, wrap=tk.WORD, width=40, height=15)
        content_text.pack()
        content_text.insert("1.0", content)

        edit_button = tk.Button(edit_entry_window, text="Edit Entry", command=edit_entry)
        edit_button.pack()
