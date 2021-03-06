from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CreateUpdate(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User)

    class Meta:
        abstract = True

    
class Gender(CreateUpdate):
    name = models.CharField(verbose_name = "Sex", max_length = 255)

    class meta:
        verbose_name_plural = 'gender/sex'

    def __str__(self):
        return self.name

    
class MaritalStatus(CreateUpdate):
    name = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = 'marital status'

    def __str__(self):
        return self.name

    
class Person(CreateUpdate):
    first_name = models.CharField(max_length=255, verbose_name="First name")
    surname = models.CharField(max_length=255, verbose_name="Surname")
    othername = models.CharField(max_length=255, blank=True, verbose_name="Othername")
    home_village = models.CharField(max_length=255, blank = True, verbose_name="Home Village")
    person_photo = models.ImageField(upload_to = 'person_photos', null=True, blank=True, verbose_name = "Passport Photo")

    class Meta:
        ordering = ['-updated', 'surname']
        verbose_name_plural = "persons"

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.surname, self.othername)

    
class PersonDemographic(CreateUpdate):
    gender = models.ForeignKey(Gender, blank = True)
    date_of_birth = models.DateField(blank = True)
    marital_status = models.ForeignKey(MaritalStatus, blank=True)
    person = models.ForeignKey(Person)

    class Meta:
        verbose_name = 'demographic'

    def __str__(self):
        return "{} {}".format(self.person, self.gender)

    
class PersonGuardian(CreateUpdate):
    father_name = models.CharField(max_length=255, blank=True, verbose_name="Father's Name")
    mother_name = models.CharField(max_length=255, blank=True, verbose_name="Mother's Name")
    guardian_occupation = models.CharField(max_length=255, blank=True)
    person = models.ForeignKey(Person)

    class Meta:
        verbose_name = 'guardian/next of kin'

    def __str__(self):
        return "{} {} {}".format(self.person, self.father_name, self.mother_name)

    
class PersonContacts(CreateUpdate):
    telephone = models.CharField(max_length=255, blank=True, verbose_name="Telephone (Mobile)")
    mailing_address = models.CharField(max_length=255, blank=True, verbose_name="Mailing Address")
    residence = models.CharField(max_length=255, blank=True)
    person = models.ForeignKey(Person)

    class Meta:
        verbose_name='person contact'

    def __str__(self):
        return "{} {}".format(self.person, self.telephone)

    
class PersonVitals(CreateUpdate):
    body_temperature = models.FloatField(blank=True, help_text="Temperature in Degrees Celcius")
    blood_pressure = models.FloatField(blank=True)
    weight = models.FloatField(blank=True)
    person = models.ForeignKey(Person)

    class Meta:
        verbose_name = 'vital'

    def __str__(self):
        return "{} {}".format(self.person, self.body_temperature, self.weight)
