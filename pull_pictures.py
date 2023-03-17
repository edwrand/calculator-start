import os
import shutil

# define the source directory that contains all the photos
source_dir = "/Users/ebbyrandall/Desktop"

# define the destination directory where all photos will be moved
destination_dir = "/Users/ebbyrandall/Desktop/all_photos"

# create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# move all photos from the source directory to the destination directory
for filename in os.listdir(source_dir):
    if (
        filename.endswith(".jpg")
        or filename.endswith(".png")
        or filename.endswith(".jpeg")
        or filename.endswith(".webp")
    ):
        shutil.move(
            os.path.join(source_dir, filename), os.path.join(destination_dir, filename)
        )
