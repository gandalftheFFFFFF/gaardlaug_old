from django.db import models
from django.utils import timezone

import datetime

# Create your models here.


class BoardMember(models.Model):
    """ This class represents a single board members; his name and address
    as well as date of entry/exit
    """
    first_name = models.CharField(max_length=200, default='first name')
    last_name = models.CharField(max_length=200, default='last name')
    street_name = models.CharField(max_length=200)
    street_number = models.IntegerField(blank=True, null=True)
    street_number_letter = models.CharField(max_length=10, blank=True, null=True)
    from_date = models.DateField(default=datetime.date.today)
    to_date = models.DateField(blank=True, null=True)
    # role = models.ForeignKey(Role, null=True, blank=True)

    def __str__(self):
        return '{last}, {first}'.format(last=self.last_name, first=self.first_name)

    def is_active(self):
        return not self.to_date or self.to_date > datetime.date.today()

    is_active.boolean = True

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['first_name']


class Role(models.Model):
    """ This class represents the different roles board members can have
    such as treasurer, etc.
    """
    role = models.CharField(max_length=200)
    board_member = models.ForeignKey(BoardMember, null=True, blank=True)

    def __str__(self):
        return self.role

class Cadastre(models.Model):
    """ This class represents a simple cadastre (matrikel)
    """
    cadastre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cadastre_name

    class Meta:
        ordering = ['cadastre_name']
