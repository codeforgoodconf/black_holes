from django.test import TestCase
from tinder.src.DbController import DbController

from tinder.models import Galaxy

# Create your tests here.

class TestDbControls(TestCase):
    def setUp(self):
        Galaxy.objects.create(human_label=None, file_url="sldkjf")

    def test_gets_galaxies(self):
        db = DbController()
        # import pdb; pdb.set_trace()
        galaxy = db.next_unlabeled_galaxy()

        self.assertIsInstance(galaxy, Galaxy)
