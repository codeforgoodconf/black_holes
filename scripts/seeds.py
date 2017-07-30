from app.db import db, Galaxy
import os
from app.db.controls import Controller


# load all filenames in spectrum_data folder
# add a row for each file
def get_file_list(path):
    file_list = os.listdir(path)
    return file_list

def rm_fits(filename):
    a = filename.replace(".fits", "")
    return a


def seed_db():
    print("SEED DB")

    db.drop_all()
    db.create_all()

    DIR = "spectrum_data"
    file_list = get_file_list(DIR)
    print(file_list)
    file_list = [rm_fits(filename) for filename in file_list]
    print(file_list)
    controller = Controller()
    galaxies = [controller.create_new_galaxy(f"{filename}") for filename in file_list]

    db.session.add_all(galaxies)
    db.session.commit()

    print(Galaxy.query.all())
