import os
import shutil

def delete_folders_and_files(root_folder, folders_to_delete, files_to_delete):
    for foldername, subfolders, filenames in os.walk(root_folder):
        # Exclude .venv folder from traversal
        if '.venv' in subfolders:
            subfolders.remove('.venv')
        
        for folder_to_delete in folders_to_delete:
            if folder_to_delete in subfolders:
                folder_path = os.path.join(foldername, folder_to_delete)
                print(f"Deleting {folder_path}")
                shutil.rmtree(folder_path)
                print(f"{folder_path} deleted successfully")

        for file_to_delete in files_to_delete:
            if file_to_delete in filenames:
                file_path = os.path.join(foldername, file_to_delete)
                print(f"Deleting {file_path}")
                os.remove(file_path)
                print(f"{file_path} deleted successfully")

root_folder = './'

folders_to_delete = ['migrations', '__pycache__']

files_to_delete = ['db.sqlite3']

delete_folders_and_files(root_folder, folders_to_delete, files_to_delete)
