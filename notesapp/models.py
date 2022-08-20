from django.db import models

class NotesModel(models.Model):
    title=models.CharField(max_length=120, primary_key=True)
    note=models.CharField(max_length=19999)
    image=models.ImageField(upload_to="images", null=True)