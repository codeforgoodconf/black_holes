import pytest


import os
from scripts.seeds import get_file_list


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
