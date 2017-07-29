from app.db import db, Galaxy
import os



# load all filenames in spectrum_data folder
# add a row for each file
def get_file_list(path):
    file_list = os.listdir(path)
    return file_list




def create_new_galaxy(path):
    galaxy = Galaxy(
        label_lower=None,
        label_upper=None,
        file_url=path,
        tf_value=None,
        tf_label=None,
        human_label=None)

    return galaxy






def seed_db():
    print("SEED DB")

    db.drop_all()
    db.create_all()

    DIR = "spectrum_data"
    file_list = get_file_list(DIR)

    galaxies = [create_new_galaxy(f"{DIR}/{filename}") for filename in file_list]

    db.session.add_all(galaxies)
    db.session.commit()

    print(Galaxy.query.all())




