# Create a command-line application for performing backups of a file or folder. The application should allow the user to specify the source and destination and automatically detect whether the source is a file or a folder. Additionally, the user should be able to choose between compressed or uncompressed backup. After the backup, the application should send an email with information about the backup, including success status, the number of files backed up, source, destination, and the name or names of the backed-up files


### Ushtrimi 1 ###
# krijoni nje command line application qe mundeson kryerjen e backup
# te nje file ose te nje folder.
# Aplikacioni duhet te lejoj perdoruesin te percaktoj source dhe destination
# dhe gjithashtu do detektoj automatikisht nese source eshte nje file ose nje folder.
# Aplikacioni do i lejoj perdoruesit te percaktoj nese do qe ta ruaj backup-in compressed
# apo uncompressed.
# Ne perfundim te backup-it aplikacioni do dergoj nje email me informacione nga backup-i
# (nese backup-i u krye apo jo me sukses, sa file jane bere backup, source, destination,
# emrin e file ose fileve qe jan bere backup dhe gjithashtu permasat e backup-it).
# Aplikacioni gjithashtu duhet te marri parasysh te gjitha exceptions te mundshme dhe ti
# kthej perdoruesit mesazhe errori perkatese.

# file ose folderi i cili do behet backup do ruhet me emrin:
# [datetime]-[source-file or source-folder].[file extension or "zip" if it is compressed]

# shembull:  backup.py C:/Users/user/Desktop/file.txt  C:/ --zip
# (backup i nje file te kompresuar)
#    ->  backup name:  2023-07-06 20:00:00 file.zip

# shembull:  backup.py C:/Users/user/Desktop/New Folder  C:/backup_folder
# (backup i nje file te kompresuar)
#    ->  backup name:  2023-07-06 20:00:00 New Folder

# per cli arguments mund te perdorni sys.arg  (ose argparse)


################## D.SH: implementoni funksionalitetin e dergimit te email ##############


import argparse
import os
import shutil
import sys
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("source_dir", help="The file or folder source path.")
parser.add_argument("destination_dir", help="The destination directory path.")
parser.add_argument(
    "-z", "--zip", help="Compress the file/folder.", action="store_true"
)
args = parser.parse_args()


def get_folder_name_from_path(path):
    return os.path.basename(os.path.normpath(path))


if not os.path.exists(args.source_dir):
    sys.exit("The source path does not exist!")

if not os.path.isdir(args.destination_dir):
    sys.exit("The destination path is either a file or does not exist as a folder!")


if os.path.isfile(args.source_dir):
    print("The source is a file!")
    try:
        if args.zip:  # this dos not work correctly ###### D.sh: FIX IT ######
            filename = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {os.path.basename(args.source_dir)}"
            destination_filename = os.path.join(args.destination_dir, filename)
            shutil.make_archive(destination_filename, "zip", args.source_dir)
            print("File copied successfully. (Compressed with zip format)")
        else:
            shutil.copy(args.source_dir, args.destination_dir)
            backup_file_path = os.path.join(
                args.destination_dir, os.path.basename(args.source_dir)
            )
            backup_file_new_name = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {os.path.basename(args.source_dir)}"
            os.rename(
                backup_file_path,
                os.path.join(args.destination_dir, backup_file_new_name),
            )
            print("File copied successfully. (Uncompressed)")
    except shutil.SameFileError:
        print("The source is the same as the destination!")

else:
    print("The source is a folder!")
    try:
        if args.zip:
            folder_name = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {get_folder_name_from_path(args.source_dir)}"
            destination_folder_name = os.path.join(args.destination_dir, folder_name)
            shutil.make_archive(destination_folder_name, "zip", args.source_dir)
            print("Folder copied successfully. (Compressed with zip format)")
        else:
            dir_name = get_folder_name_from_path(
                args.source_dir
            )  # devops_python_scripting
            new_directory_path = os.path.join(
                args.destination_dir, dir_name
            )  # /home/damiano/SDA/backup/devops_python_scripting
            shutil.copytree(args.source_dir, new_directory_path)

            backup_folder_path = os.path.join(
                args.destination_dir,
                get_folder_name_from_path(args.source_dir),
            )
            backup_folder_new_name = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {get_folder_name_from_path(args.source_dir)}"
            os.rename(
                backup_folder_path,
                os.path.join(args.destination_dir, backup_folder_new_name),
            )
            print("Folder copied successfully.")
    except shutil.SameFileError:
        print("The source is the same as the destination!")
