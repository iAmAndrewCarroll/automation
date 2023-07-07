from rich.console import Console
from rich.prompt import Prompt
import sys
import os
from automation.createFolder import create_folder
from automation.deleteUser import move_user_documents
from automation.sortDocuments import sort_documents
from automation.warningParse import parse_log_file
from automation.countingFiles import count

def main():
  console = Console()
  while True:
    # os.system('clear')
    console.print(f'\n1. Create a folder: \n2. Delete a user: \n3. Sort Documents: \n4. Parse a log file: \n5. Specific file-type amount: \n(q) Quit', style='bold blue')
    choice = Prompt.ask('Enter your choice', choices=['1', '2', '3', '4', '5', 'q'], default='q')
    
    if choice == '1':
      folder_name = Prompt.ask("Enter folder name")
      create_folder(folder_name)
      
    elif choice == '2':
      folder = Prompt.ask("Enter folder name")
      file = Prompt.ask("Enter file name")
      if os.path.exists(f'{folder}/{file}'):
        move_user_documents(folder, file)
        console.print(f"File '{file}' moved to temp folder!", style="bold green")
      else:
        console.print(f"Either folder or file does not exist!", style="bold red")
        
    elif choice == '3':
      folder_path = Prompt.ask("Enter folder path")
      if os.path.exists(folder_path):
        sort_documents(folder_path)
      else:
        print(f"Folder {folder_path} does not exist!")
        
    elif choice == '4':
      log_file_path = Prompt.ask("Enter log file path")
      if os.path.exists(log_file_path):
        parse_log_file(log_file_path, "logs")
      else:
        console.print(f"Log file does not exist!", style="bold red")
        
    elif choice == '5':
      file_extension = Prompt.ask("Enter file extension")
      folder_path = Prompt.ask("Enter folder path")
      if os.path.exists(folder_path):
        console.print(f"Number of {file_extension} files in {folder_path} is {count(file_extension, folder_path)}", style="bold green")
      else:
        console.print(f"Folder {folder_path} does not exist!", style="bold red")
        
    elif choice == 'q' or 'Q':
      do_exit('Exiting...')
    else:
      print('Try Again')
      
def do_exit(message):
  sys.exit(message)
  
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    do_exit('Ctrl+C detected! Exiting...')
    