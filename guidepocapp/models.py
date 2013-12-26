from django.db import models


class Region(models.Model):
    description = models.CharField(max_length=512)
    region_name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.region_name


class Place(models.Model):
    x_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    y_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    place_name = models.CharField(max_length=200)
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return self.place_name


# Need to define fields guide needs
# surname, name, phone1, phone2, skype, www, places (multiple choise to fill GuideToPlace table),
#  activity*, comments/info, pwd, email/login
class Guide(models.Model):
    email = models.CharField(max_length=60)
    pwd = models.CharField(max_length=20)

    activity = models.CharField(max_length=20, default='')

    surname = models.CharField(max_length=60, default='')
    name = models.CharField(max_length=60, default='')
    phone1 = models.CharField(max_length=20, default='')
    phone2 = models.CharField(max_length=20, default='')
    skype = models.CharField(max_length=40, default='')
    comments = models.CharField(max_length=2048, default='')

    def __unicode__(self):
        return self.email


class GuideToPlace(models.Model):
    place_id = models.ForeignKey(Place)
    guide_id = models.ForeignKey(Guide)


