from django.db import models

# Create your models here.




#
#
# id = db.Column(db.Integer, primary_key=True)
# label_lower = db.Column(db.Float)
# label_upper = db.Column(db.Float)
# file_url = db.Column(db.String)
# tf_value = db.Column(db.Float)
# tf_label = db.Column(db.Boolean)
# human_label = db.Column(db.Boolean)
#



class Galaxy(models.Model):
    id = models.IntegerField(primary_key=True)
    file_url = models.TextField()
    tf_value = models.FloatField(null=True)
    tf_label = models.NullBooleanField()
    human_label = models.NullBooleanField()




