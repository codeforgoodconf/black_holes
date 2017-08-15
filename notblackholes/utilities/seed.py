import os
import json

from config import DATA_ROOT

FIXTURE_PATH = "tinder/fixtures/galaxy.json"
 # TODO: convert to using config.py in root dir


# load all filenames in spectrum_data folder

def get_file_list(path):
    file_list = os.listdir(path)
    return file_list


def rm_fits(filename):
    a = filename.replace(".fits", "")
    return a


def galaxy_json(dir, filename, label):
    return {
        "model": "tinder.Galaxy",
        "fields": {
            "file_url": filename,
            "original_root_extension": dir,
            "human_label": label
        }
    }


def process_data_dir(dir, label):
    file_list = get_file_list(os.path.join(DATA_ROOT, dir))
    file_list = [rm_fits(filename) for filename in file_list]
    galaxies = [galaxy_json(dir, filename, label) for filename in file_list]
    return galaxies


def seed_db():
    print("Create DB fixtures of Galaxy")

    galaxies = process_data_dir("positives", 1) + \
               process_data_dir("negatives", 0) + \
               process_data_dir("unlabeled", None)

    with open(FIXTURE_PATH, "w") as file:
        json.dump(galaxies, file)


if __name__ == "__main__":
    seed_db()
