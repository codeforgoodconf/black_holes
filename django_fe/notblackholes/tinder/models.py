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
    file_url = models.FloatField()
    tf_value = models.FloatField()
    tf_label = models.BooleanField()
    human_label = models.BooleanField()



