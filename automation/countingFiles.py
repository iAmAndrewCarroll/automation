from rich.console import Console
from rich.prompt import Prompt
import os
import shutil

# Counting the number of specific file types in a directory.

console = Console()
prompt = Prompt()

def count(file_extension, folder_path):
  files = os.listdir(folder_path)
  count = 0
  for file in files:
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
      if os.path.splitext(file)[1] == file_extension:
        count += 1
  return count

if __name__ == "__main__":
  # should work with any file extension
  file_extension = Prompt.ask("Enter file extension")
  folder_path = Prompt.ask("Enter folder path")
  if os.path.exists(folder_path):
    console.print(f"Number of {file_extension} files in {folder_path} is {count(file_extension, folder_path)}", style="bold green")
  else:
    console.print(f"Folder {folder_path} does not exist!", style="bold red")
    