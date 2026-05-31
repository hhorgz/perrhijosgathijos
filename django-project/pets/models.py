from django.contrib.auth.models import User
from django.db import models

class IdType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Personality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AgeType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Species(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FosterParent(models.Model):
    id_type = models.ForeignKey(IdType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    official_id = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Profile(models.Model):
    foster_parent = models.ForeignKey(FosterParent, on_delete=models.CASCADE)
    personality = models.ForeignKey(Personality, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    age_type = models.ForeignKey(AgeType, on_delete=models.CASCADE)
    sex = models.CharField(
        max_length=1,
        choices=(('M', 'M'), ('F'   , 'F')),
        default=1,
    )
    resumen = models.TextField()
    #photo = models.ImageField(upload_to='profile_pics')
    pub_date = models.DateTimeField('date published')
    is_adopted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    adoption_date = models.DateTimeField('date adopted', blank=True, null=True)

    def __str__(self):
        return self.name