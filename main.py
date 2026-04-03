from pathlib import Path
# This is for having the creation date of a file in a human readable format (instead of like 1771616739.0072565) and iterating on it I think too
from datetime import datetime
# Thing I need to move files between drives
import shutil
# Moved constants to a separate file to make it easier to edit and read the main code
from constants import BASE_DIR, FILE_FORMATS, months_formats_dict


# rglob with the star loops through all the files in a given path. is case sensitive by default. I'm not sure if all photos have small jpg or if some have JPG.
# rglob is wrapped in a list to prevent it from looping over files it already moved 
for p in list(Path(BASE_DIR).rglob('*')):
    print(f"--- Checking: {p.name} ---")
    if p.suffix.lower() in FILE_FORMATS:
        print(f"✅ Match found: {p.name}")
        # Those 2 lines are I think needed to convert the unix weird date numbers to a human data that I can do stuff with like call just the day from it etc.
        # ctime is creation and mtime is Modification. Both seem to be flawed. Will need to test.
        timestamp = p.stat().st_mtime
        creation_date = datetime.fromtimestamp(timestamp)
        
        # Format for my year folders
        year_folder = creation_date.strftime("%Y")

        # Format for my month folders
        month_num = creation_date.month
        month_name = months_formats_dict[month_num]
        month_folder = f"{month_num:02d} - {month_name}"
        
        # Format for my final folder for the dates
        day_folder = creation_date.strftime("%d.%m.%y -")

        # Final destination path
        final_path = BASE_DIR / year_folder / month_folder / day_folder
        print(f"📂 Destination: {final_path}")
        if p.exists():
            #Creates a whole folder path if it doesn't exist yet
            final_path.mkdir(parents=True, exist_ok=True)
            print(f"🚀 Copying {p.name} now...")
            # Can change to move instead of copy to test it out in the real world first.
            # It takes 2 arguments - the source we're moving and the destination path.
            shutil.copy(p, final_path / p.name)
            print("Done!")
        else:
            print(f"❌ Skipped (wrong format): {p.suffix}")   