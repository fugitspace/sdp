from django import forms
from django.contrib.auth.models import User

from person.models import Person, PersonVitals, PersonDemographic, PersonGuardian, PersonContacts

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'surname', 'othername', 'home_village', 'person_photo')
        widgets = {
            'person_photo' : forms.ClearableFileInput(attrs={'accept': 'image/*', 'name':'image'}),
        }

class PersonVitalsForm(forms.ModelForm):
    class Meta:
        model = PersonVitals
        fields = ('body_temperature', 'blood_pressure', 'weight')


class PersonDemographicForm(forms.ModelForm):
    class Meta:
        model = PersonDemographic
        fields = ('gender', 'date_of_birth', 'marital_status')


class PersonContactForm(forms.ModelForm):
    class Meta:
        model = PersonContacts
        fields = ('telephone', 'mailing_address', 'residence')


class PersonNextofKinForm(forms.ModelForm):
    class Meta:
        model = PersonGuardian
        fields = ('father_name', 'mother_name', 'guardian_occupation')
