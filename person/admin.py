from django.contrib import admin
from person.models import Gender, MaritalStatus, Person, PersonDemographic, PersonGuardian, PersonVitals, PersonContacts
# Register your models here.

admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(Person)
admin.site.register(PersonDemographic)
admin.site.register(PersonGuardian)
admin.site.register(PersonVitals)
admin.site.register(PersonContacts)
