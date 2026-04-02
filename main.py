from pathlib import Path
# This is for having the creation date of a file in a human readable format (instead of like 1771616739.0072565) and iterating on it I think too
from datetime import datetime

# Define the base directory, which should the parent of the parent of this file (the python file should be on my Desktop)
BASE_DIR = Path(__file__).resolve().parent.parent

# This gets all the way to the root and home directory I think which might be useful in the future
# BASE_DIR = Path("..").resolve()
# BASE_DIR = Path.home()

# ok I think this is it. rglob is case sensitive by default. I'm not sure if all photos have small jpg or if some have JPG.
for p in Path(BASE_DIR).rglob('*', case_sensitive=False):
    if p.suffix in (".py", ".pyc", ".jpg", ".png", ".RW2", ".RAF", ".DNG", ".mp4", ".mov"):
        # Those 2 lines are I think needed to convert the unix weird date numbers to a human data that I can do stuff with like call just the day from it etc.
        timestamp = p.stat().st_ctime
        creation_date = datetime.fromtimestamp(timestamp)
        # Showcase of what we can cook with this datetime
        print(creation_date.day, creation_date.month, creation_date.year, creation_date, " - ", p)
        
        # Format for my folder right under Photo Video with a year
        print(creation_date.strftime("%Y"))

        # Format for my month folders. Idk if it can be done less clunkly as I have them in polish so my idea is to have an if statement for each month
        if creation_date.month == 1:
            print(creation_date.strftime("%m - styczeń"))
        elif creation_date.month == 2:
            print(creation_date.strftime("%m - luty"))
        elif creation_date.month == 3:
            print(creation_date.strftime("%m - marzec"))
        elif creation_date.month == 4:
            print(creation_date.strftime("%m - kwiecień"))
        elif creation_date.month == 5:
            print(creation_date.strftime("%m - maj"))
        elif creation_date.month == 6:
            print(creation_date.strftime("%m - czerwiec"))
        elif creation_date.month == 7:
            print(creation_date.strftime("%m - lipiec"))
        elif creation_date.month == 8:
            print(creation_date.strftime("%m - sierpień"))
        elif creation_date.month == 9:
            print(creation_date.strftime("%m - wrzesień"))
        elif creation_date.month == 10:
            print(creation_date.strftime("%m - październik"))
        elif creation_date.month == 11:
            print(creation_date.strftime("%m - listopad"))
        elif creation_date.month == 12:
            print(creation_date.strftime("%m - grudzień"))
        
        # Format for my final folder for the dates
        print(creation_date.strftime("%d.%m.%y - "))