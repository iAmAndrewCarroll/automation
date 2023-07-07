from rich.console import Console
from rich.prompt import Prompt
import sys
import os
from automation.createFolder import create_folder

def main():
  console = Console()
  while True:
    os.system('clear')
    console.print(f'\n1. Create a folder: \n2. Delete a user: \n3. Sort Documents: \n4. Parse a log file: \n5. Specific file-type amount: \n(q) Quit', style='bold blue')
    choice = Prompt.ask('Enter your choice', choices=['1', '2', '3', '4', '5', 'q'], default='q')
    
    if choice == '1':
      folder_name = Prompt.ask("Enter folder name")
      create_folder(folder_name)
    elif choice == '2':
      # folder = Prompt.ask("Enter folder name")
      # file = Prompt.ask("Enter file name")
      # if os.path.exists(f'{folder}/{file}'):
      #   move_user_documents(folder, file)
      #   console.print(f"File '{file}' moved to temp folder!", style="bold green")
      # else:
      #   console.print(f"Either folder or file does not exist!", style="bold red")