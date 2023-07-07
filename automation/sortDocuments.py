from rich.prompt import Prompt
import os
import shutil

# Sort documents into appropriate folders.
# Go through a given folder and sort the documents into additional folders based on their file type.
# Move log files into a logs folder. If a logs folder doesn’t exist, your script should create one.
# Move email files into a mail folder. If a mail folder doesn’t exist, your script should create one.

prompt = Prompt()

def sort_documents(folder_path):
  
  root_directory = os.path.dirname(folder_path)
  
  logs_folder = os.path.join(root_directory, "logs")
  mail_folder = os.path.join(root_directory, "mail")
  os.makedirs(logs_folder, exist_ok=True)
  os.makedirs(mail_folder, exist_ok=True)
  
  # get all files in given folder
  files = os.listdir(folder_path)
  
  for file in files:
    file_path = os.path.join(folder_path, file)
    # check if it's a file
    if os.path.isfile(file_path):
      file_extension = os.path.splitext(file)[1]
      # move log files to logs folder
      if file_extension == '.txt':
        shutil.move(file_path, os.path.join(logs_folder, file))
        print(f'Moved {file} to logs folder')
        
      # move email files to mail folder
      elif file_extension == '.mail':
        shutil.move(file_path, os.path.join(mail_folder, file))
        print(f'Moved {file} to mail folder')
        
#write a main gate that asks for folder path and checks if it exists
if __name__ == "__main__":
  folder_path = Prompt.ask("Enter folder path")
  if os.path.exists(folder_path):
    sort_documents(folder_path)
  else:
    print(f"Folder {folder_path} does not exist!")