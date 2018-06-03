from django.contrib import admin
from vegspotapi.models import Person, Venue, Review

admin.site.register(Person)
admin.site.register(Venue)
admin.site.register(Review)
