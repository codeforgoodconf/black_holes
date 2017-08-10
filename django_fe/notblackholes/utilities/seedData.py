import os
import json

FIXTURE_PATH = "tinder/fixtures/galaxy.json"
DIR = "../../blackhole_spectra"  # TODO: convert to using config.py in root dir


# load all filenames in spectrum_data folder

def get_file_list(path):
    file_list = os.listdir(path)
    return file_list


def rm_fits(filename):
    a = filename.replace(".fits", "")
    return a


def galaxy_json(filename, label):
    return {
        "model": "tinder.Galaxy",
        "fields": {
            "file_url": filename,
            "human_label": label
        }
    }


def process_data_dir(dir, label):
    file_list = get_file_list(dir)
    file_list = [rm_fits(filename) for filename in file_list]
    galaxies = [galaxy_json(filename, label) for filename in file_list]
    return galaxies


def seed_db():
    print("Create DB fixtures of Galaxy")

    galaxies = process_data_dir(f"{DIR}/positives", 1) + process_data_dir(f"{DIR}/negatives", 0)

    with open(FIXTURE_PATH, "w") as file:
        json.dump(galaxies, file)


if __name__ == "__main__":
    seed_db()
