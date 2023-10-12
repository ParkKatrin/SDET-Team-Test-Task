# Imports
from datetime import datetime
import argparse
import shutil
import time
import os

def synchronize_folders ( folder_origin, folder_replica, path, name):
    '''
    This function will synchronize the original folder with the replica's one. 
    It will create the new information of original's path to replica's path, besides that it will also recognize if the file is still on the original's path, if
    it isn't , then the program will delete the incongruent file/directory.  
    :param folder_origin: Path to the origin folder
    :param folder_replica: Path to the replica folder
    :param path: Path to the log file
    :param name: Name of the log file
    '''
    for root, dirs, files in os.walk(folder_origin):
        for dir in dirs:
            # Identify the directory paths in the original's directory
            origin_dir_path = os.path.join(root, dir)
            relative_path = os.path.relpath(origin_dir_path, folder_origin)
            replica_dir_path = os.path.join(folder_replica, relative_path)


            if not os.path.exists(replica_dir_path):
                # Copy the directory in the replica's folder if it doesn't exist
                shutil.copytree(origin_dir_path, replica_dir_path)
                log_save(path,name, f"Created directory: {relative_path}")

        for file in files:
            # Identify the file's paths in the original's directory
            file_origin_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_origin_path, folder_origin)
            file_replica_path = os.path.join(folder_replica, relative_path)

            if not os.path.exists(file_replica_path) or (os.path.exists(file_replica_path) and os.path.getmtime(file_origin_path) > os.path.getmtime(file_replica_path)):
                # Copy the file in the replica's folder if it doesn't exist
                shutil.copy2(file_origin_path, file_replica_path)
                log_save(path,name, f"Copied file: {relative_path}")

    for root, dirs, files in os.walk(folder_replica):
        for dir in dirs:
            # Identify the directory paths in the replica's directory
            replica_dir_path = os.path.join(root, dir)
            relative_path = os.path.relpath(replica_dir_path, folder_replica)
            origin_dir_path = os.path.join(folder_origin, relative_path)

            if not os.path.exists(origin_dir_path):
                # Remove directories from replica if it doesn't exist in the original folder
                shutil.rmtree(replica_dir_path)
                log_save(path,name, f"Removed directory: {relative_path}")


        for file in files:
            # Identify the files path in the replica's directory
            file_replica_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_replica_path, folder_replica)
            file_origin_path = os.path.join(folder_origin, relative_path)

            if not os.path.exists(file_origin_path):
                # Remove the file from replica if it doesn't exist in the original folder
                os.remove(file_replica_path)
                log_save(path,name, f"Removed file: {relative_path}")

        


def log_save(path,name,message):
    '''
    This function will save the log's from de prompt command into a .log file. The user choose the name and the path 
    of that log. It will record all deleted and created files and directories and the time it occurred.  
    :param path: Path to the log file
    :param name: Name of the log file
    :param message: File/directory name
    '''
    time_info =  datetime.now().strftime("%d-%m-%Y %H:%M:%S") # Gets current time
    log_info = f"{time_info} - {message}\n" # Write the date, time and the information of the file/directory
    print(log_info)
    with open(path+name, "a") as file:
        file.write(log_info) # Write on the file all the information


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='test_task', description='This program  synchronizes two folders: origin and replica')
    parser.add_argument("folder_origin", help = "Path to the origin folder")
    parser.add_argument("folder_replica", help = "Path to the replica folder")
    parser.add_argument("sync_interval", type=int, help = "Synchronization interval in seconds")
    parser.add_argument("path_log_file", help = "Path to the log file")
    parser.add_argument("name_log_file", help = "Name of the log file")

    args = parser.parse_args()
    if args.path_log_file[-1] != '\\':
        # Checks if the path is valid
        path_final_log_file = args.path_log_file + '\\'
    else:
        path_final_log_file = args.path_log_file

    while True:
        synchronize_folders ( args.folder_origin, args.folder_replica, path_final_log_file, args.name_log_file)        
        time.sleep(args.sync_interval) 
    
        
