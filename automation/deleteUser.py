from rich.console import Console
from rich.prompt import Prompt
import os
import shutil

# Handle a deleted user.
#move user2 files into temp folder

console = Console()
prompt = Prompt()

def move_user_documents(folder, file):
  os.makedirs("temp", exist_ok=True)
  shutil.move(f'{folder}/{file}', "temp")

if __name__ == "__main__":
  folder = Prompt.ask("Enter folder name")
  file = Prompt.ask("Enter file name")
  if os.path.exists(f'{folder}/{file}'):
    move_user_documents(folder, file)
    console.print(f"File '{file}' moved to temp folder!", style="bold green")
  else:
    console.print(f"Either folder or file does not exist!", style="bold red")