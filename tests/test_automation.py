import pytest
from unittest.mock import patch, Mock
from rich.prompt import Prompt
from rich.console import Console
from automation.createFolder import create_folder
from automation.deleteUser import move_user_documents
from automation.sortDocuments import sort_documents
from automation.warningParse import parse_log_file
from automation.countingFiles import count

def test_automation():
  assert True

def test_create_folder():
  with patch('automation.createFolder.os.mkdir') as mock_mkdir:
    folder_name = "test_folder"
    create_folder(folder_name)
    mock_mkdir.assert_called_once_with(folder_name)

def test_move_user_documents_folder_and_file_exist():
  with patch('automation.deleteUser.shutil.move') as mock_move:
    folder = "test_folder"
    file = "test_file.txt"
    move_user_documents(folder, file)
    mock_move.assert_called_once_with(f'{folder}/{file}', "temp")
