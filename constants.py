from pathlib import Path

# Define the base directory, which should the parent of the parent of this file (the python file should be on my Desktop)
#BASE_DIR = Path("/mnt/c/Users/me/Desktop/Nieuporządkowane").resolve()
BASE_DIR = Path(__file__).resolve().parent

# Keeping formats here so I can edit them easly
FILE_FORMATS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".rw2",
    ".raf",
    ".dng",
    ".mp4",
    ".mov"            
)

# Dictionary for polish month dates
months_formats_dict = {
    1: "styczeń",
    2: "luty",
    3: "marzec",
    4: "kwiecień",
    5: "maj",
    6: "czerwiec",
    7: "lipiec",
    8: "sierpień",
    9: "wrzesień",
    10: "październik",
    11: "listopad",
    12: "grudzień"
}

# This gets all the way to the root and home directory I think which might be useful in the future
# BASE_DIR = Path("..").resolve()
# BASE_DIR = Path.home()