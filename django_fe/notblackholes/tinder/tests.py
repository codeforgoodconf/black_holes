from django.test import TestCase
from tinder.src.DbController import DbController

from tinder.models import Galaxy

# Create your tests here.

class TestDbControls(TestCase):
    def setUp(self):
        Galaxy.objects.create(human_label=None, file_url="sldkjf")

    def test_gets_unlabeled_galaxies(self):
        db = DbController()
        galaxy = db.next_unlabeled_galaxy()

        self.assertIsInstance(galaxy, Galaxy)

    def test_unlabeled_galaxy_has_no_human_label(self):
        db = DbController()
        galaxy = db.next_unlabeled_galaxy()

        self.assertIsNone(galaxy.human_label)

    def test_returns_false_if_all_labelled(self):
        db = DbController()
        galaxies = Galaxy.objects.all()
        for galaxy in galaxies:
            galaxy.human_label = True
            galaxy.save()

        galaxy = db.next_unlabeled_galaxy()
        self.assertFalse(galaxy)

    def test_next_machine_labelled(self):
        self.assert_("Test that next_machine_labeled_galaxy returns galaxies with tf_label and no human label")
        self.assert_("Test that if there are none matching above criterion, it returns False")

    def test_add_machine_label(self):
        self.assert_("Test that the thresholder works as we expect")

    def test_add_galaxy(self):
        before = Galaxy.objects.count()

        db = DbController()
        db.add_galaxy("assdf", True, True)

        self.assertEqual(Galaxy.objects.count(), before+1)

    def test_update_human_label_false(self):
        new_galaxy = Galaxy.objects.create(file_url="somefile", human_label=None)
        new_galaxy.save()
        id = new_galaxy.id

        db = DbController()
        db.update_human_label(id, 0)

        my_galaxy = Galaxy.objects.get(id=id)
        self.assertFalse(my_galaxy.human_label)

    def test_update_human_label_true(self):
        new_galaxy = Galaxy.objects.create(file_url="somefile", human_label=None)
        new_galaxy.save()
        id = new_galaxy.id

        db = DbController()
        db.update_human_label(id, 1)

        my_galaxy = Galaxy.objects.get(id=id)
        self.assertTrue(my_galaxy.human_label)

    def test_update_affirmation_label_true(self):
        new_galaxy = Galaxy.objects.create(file_url="somefile", affirmation=None)
        new_galaxy.save()
        id = new_galaxy.id

        db = DbController()
        db.update_machine_affirmation(id, 1)

        my_galaxy = Galaxy.objects.get(id=id)
        self.assertTrue(my_galaxy.affirmation)


    def test_update_affirmation_label_false(self):
        new_galaxy = Galaxy.objects.create(file_url="somefile", affirmation=None)
        new_galaxy.save()
        id = new_galaxy.id

        db = DbController()
        db.update_machine_affirmation(id, 0)

        my_galaxy = Galaxy.objects.get(id=id)
        self.assertFalse(my_galaxy.affirmation)

