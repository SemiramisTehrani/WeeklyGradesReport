from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Report(models.Model) :
    courses          = models.CharField(max_length = 255)
    grades           = models.CharField(max_length = 255)
    date             = models.CharField(max_length = 255)
    