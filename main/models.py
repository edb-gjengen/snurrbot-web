from django.db import models

class Entry(models.Model):
    user = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text + " (" + self.user + ", " + self.created.strftime("%Y-%m-%d %H:%M") + ")"
