from django.test import TestCase
from tinder.src.DbController import DbController

from tinder.models import Galaxy

# Create your tests here.

class TestDbControls(TestCase):
    def test_gets_galaxies(self):
        db = DbController()
        galaxy = db.next_unlabeled_galaxy()

        self.assertIsInstance(galaxy, Galaxy)
