from fit2gpx import StravaConverter
import os
import subprocess
import shutil

DIR_STRAVA = 'C:/Users/Heloise/Desktop/Strava'
DIR_BACKUP = 'C:/Users/Heloise/Desktop/Strava/backup'

# - Note: the dir_in must be the path to the central unzipped Strava bulk export folder
# - Note: You can specify the dir_out if you wish. By default it is set to 'activities_gpx', which will be created in main Strava folder specified.

strava_conv = StravaConverter(
    dir_in=DIR_STRAVA,
    dir_out=DIR_BACKUP
)

strava_conv.unzip_activities()

# --------------------------------------
# --------------------------------------
# --------------------------------------

DIR_ACT = os.path.join(DIR_STRAVA, "activities")

def convert_and_move(folder):
    path_folder = os.path.join(DIR_ACT, folder)
    extension = folder[-4:].lower()

    # - Create Babel's commands based on the extensions to check and convert if necessary
    extension_commande_map = {
        ".tcx": "gpsbabel -i gtrnctr -f {} -o gpx -F {}.gpx",
        ".fit": "gpsbabel -i garmin_fit -f {} -o gpx -F {}.gpx"
    }

    # - Run the commands and move the folder
    if extension in extension_commande_map:
        commande = extension_commande_map[extension].format(path_folder, path_folder[:-4])
        subprocess.run(commande, shell=True)
        shutil.move(path_folder, os.path.join(DIR_BACKUP, folder))

if __name__ == '__main__':
    folders = os.listdir(DIR_ACT)
    for folder in folders:
        convert_and_move(folder)

print(":)")