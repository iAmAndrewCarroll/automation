from rich.console import Console
from rich.prompt import Prompt
import os

# Automate the creation of a folder.
# Write a Python script that prompts the user for a folder name then create the folder automatically.

console = Console()
prompt = Prompt()

def create_folder(folder_name):
  try:
    os.mkdir(folder_name)
    console.print(f"Folder '{folder_name}' created successfully!", style="bold green")
  except FileExistsError:
    console.print(f"Folder '{folder_name}' already exists!", style="bold red")
    
    
if __name__ == "__main__":
  folder_name = Prompt.ask("Enter folder name")
  create_folder(folder_name)