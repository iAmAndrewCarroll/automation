from rich.prompt import Prompt
from rich.console import Console
import os
import shutil

# Parse a log file for errors and warnings.
# From the previous task, you’ve moved a log file into the logs folder. Now, parse the log file for errors and warnings and create two separate log files in a target directory:
# errors.log: Contains all error messages.
# warnings.log: Contains all warning messages.

console = Console()
prompt = Prompt()

def parse_log_file(log_file_path, target_directory):
  os.makedirs(target_directory, exist_ok=True)
  errors_log_file = os.path.join(target_directory, "errors.log")
  warnings_log_file = os.path.join(target_directory, "warnings.log")
  
  with open(log_file_path) as log_file:
    for line in log_file.readlines():
      if "ERROR" in line:
        with open(errors_log_file, "a") as errors_file:
          errors_file.write(line)
      elif "WARNING" in line:
        with open(warnings_log_file, "a") as warnings_file:
          warnings_file.write(line)
          
  console.print(f"Log file parsed successfully!", style="bold green")
  
    
if __name__ == "__main__":
  log_file_path = Prompt.ask("Enter log file path")
  if os.path.exists(log_file_path):
    parse_log_file(log_file_path, "logs")
  else:
    console.print(f"Log file does not exist!", style="bold red")