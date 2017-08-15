from django.db import models


class Galaxy(models.Model):
    # id = models.IntegerField(primary_key=True)
    file_url = models.TextField()
    original_root_extension = models.TextField()
    tf_value = models.FloatField(null=True, default=None)
    tf_label = models.NullBooleanField(null=True, default=None)
    human_label = models.NullBooleanField(null=True, default=None)
    affirmation = models.NullBooleanField(null=True, default=None)
