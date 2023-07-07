from rich.console import Console
from rich.prompt import Prompt
import sys
import os

def main():
  console = Console()
  while True:
    os.system('clear')
    console.print(f'\n1. Create a folder: \n2. Delete a user: \n3. Sort Documents: \n4. Parse a log file: \n5. Specific file-type amount: \n6. Exit', style='bold blue')