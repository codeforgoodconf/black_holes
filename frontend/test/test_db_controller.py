import pytest
from app.db.controls import DbController
from app.db import Galaxy


class TestGalaxyCreation:
    def test_returns_galaxy(self):
        galaxy = DbController().create_new_galaxy("The path")

        assert isinstance(galaxy, Galaxy)

    def test_galaxy_has_my_path(self):
        galaxy = DbController().create_new_galaxy("The path")

        assert galaxy.file_url == "The path"

    def test_new_galaxy_is_unlabeled(self):
        galaxy = DbController().create_new_galaxy("The path")

        assert galaxy.human_label == None
        assert galaxy.tf_label == None
        assert galaxy.tf_value == None
