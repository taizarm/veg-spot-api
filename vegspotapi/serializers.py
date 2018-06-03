from vegspotapi.models import Person, Venue, Review
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = ('name', )


class VenueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Venue
        fields = ('name', 'description', )


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Review
        fields = ('star', 'content', )
