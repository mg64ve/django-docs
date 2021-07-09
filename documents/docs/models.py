from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from django.utils.html import mark_safe
import time
import os.path

def get_path(instance, filename):
   fn, ext = os.path.splitext(filename)
   ts = str(int(time.time()))
   return os.path.join('{}_{}{}'.format(fn, ts, ext))

class doc(models.Model):
    doc_name = models.CharField(max_length=30, verbose_name=u"doc name", help_text=u"name of the doc")
    doc_document = models.FileField(upload_to=get_path, verbose_name=u"document", help_text=u"document")

    class Meta:
        unique_together = ("doc_name", )

    def __str__(self):
        return f"{self.doc_name}"
