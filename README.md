# SDET-Team-Test-Task
## Folder Synchronization Program
This Python script was designed to synchronize two folders, the original and the replica. It performs one-way synchronization. It will make copies continuasly, adding and updating from the original folder to replica's while logging actions to a specified log file.

## Features
 - One-way synchronization
 - Supports files, directories and subdirectories
 - Periodic synchronization interval specified from the user
 - Easy to configure throught line arguments

## Command Line Arguments
This program accepts the following commands line arguments:
 - folder_origin: Path to the origin folder
 - folder_replica: Path to the replica folder
 - sync_interval: Synchronization interval in seconds (integer only)
 - path_log_file: Path to the log file
 - name_log_file: Name of the log file

   Exemple:
   python Test_Task.py path\to\origin path\to\replica 3600 path\to\log\file log_file.log

## Running the Programs
 - Run this script only on command prompt as shown above
