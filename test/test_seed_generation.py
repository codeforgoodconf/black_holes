import pytest


import os
from scripts.seeds import get_file_list, create_new_galaxy
from app.db import Galaxy

DIR = "spectrum_data"


class TestListBuilder:
    def test_get_file_list_returns_length(self):
        files = get_file_list(DIR)

        assert len(files) > 0

    def test_files_are_specs(self):
        files = get_file_list(DIR)

        assert files[0][:4] == "spec"

    def test_file_exists(self):
        files = get_file_list(DIR)
        assert os.path.isfile(f"{DIR}/{files[0]}")


class TestGalaxyCreation:
    def test_returns_galaxy(self):
        galaxy = create_new_galaxy("The path")

        assert isinstance(galaxy, Galaxy)

    def test_galaxy_has_my_path(self):
        galaxy = create_new_galaxy("The path")

        assert galaxy.file_url == "The path"

    def test_new_galaxy_is_unlabeled(self):
        galaxy = create_new_galaxy("The path")

        assert galaxy.human_label == None
        assert galaxy.tf_label == None
        assert galaxy.tf_value == None







