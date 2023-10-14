# Import OS is super important so that anyone using any operating system is able to use it
import os

# This is going to create a PersonalWiki class to manage all of the entries
class PersonalWiki:
    def __init__(self):
        self.entries = {} # This creates a dictionary to store the entries
        self.project_directory = None # Initializes the project directory

    def set_project_directory(self, project_directory): # This lets you set directories
        self.project_directory = project_directory

    def add_entry(self, title, content): #Adds an entry into the writing wiki
        self.entries[title] = content #Add entry to dictionary

        # We want to create an entries directory in project directory if it doesn't exist
        if self.project_directory:
            entries_directory = os.path.join(self.project_directory, "entries")
            if not os.path.exists(entries_directory):
                os.makedirs(entries_directory)

            entry_filename = os.path.join(entries_directory, f"{title}.txt")
            # Creates a file with the title as the filename
            with open(entry_filename, 'w') as file:
                file.write(content)
            # Writes the entry content to the file