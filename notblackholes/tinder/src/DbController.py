from random import randint

from tinder.models import Galaxy


class DbController:
    def add_many_machine_labels(self, predictions):
        for filename, value in predictions.items():
            print(f"File: {filename}, value: {value}")
            self.add_machine_label(filename, value)

    def add_galaxy(self, file_url, human_label=None, tf_label=None):
        galaxy = Galaxy(file_url=file_url,
                        human_label=human_label,
                        tf_label=tf_label)
        galaxy.save()

    def update_human_label(self, id, human_label):
        galaxy = Galaxy.objects.get(id=id)
        galaxy.human_label = human_label
        galaxy.save()

    def update_machine_affirmation(self, id, affirmation):
        galaxy = Galaxy.objects.get(id=id)
        galaxy.affirmation = affirmation
        galaxy.save()

    def next_unlabeled_galaxy(self):
        galaxies = Galaxy.objects.filter(human_label=None)

        if galaxies.count():
            galaxy = galaxies[randint(0, galaxies.count() - 1)]

            return galaxy
        else:
            return False

    def next_machine_labeled_galaxy(self):
        galaxies = Galaxy.objects.exclude(tf_label=None).exclude(human_label=None)

        if galaxies.count():
            galaxy = galaxies[randint(0, galaxies.count() - 1)]
            return galaxy
        else:
            return False

    def create_new_galaxy(self, path):
        galaxy = Galaxy(
            label_lower=None,
            label_upper=None,
            file_url=path,
            tf_value=None,
            tf_label=None,
            human_label=None
        )

        return galaxy

    def add_machine_label(self, file_url, machine_prediction):
        if file_url.endswith(".fits"):
            file_url = file_url.replace(".fits", "")

        # TODO: break thresholder into a separate function.
        galaxies = Galaxy.objects.filter(file_url=file_url)
        if galaxies.count():
            galaxy = galaxies[0] # TODO: fix this access, should be able to 'get' just the one since file_url needs to be unique.

            galaxy.tf_label = machine_prediction > 0.8
            galaxy.tf_value = machine_prediction
            galaxy.save()
