from vegspotapi.models import Person, Venue, Review
from rest_framework import viewsets
from vegspotapi.serializers import PersonSerializer, VenueSerializer, ReviewSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class VenueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows venues to be viewed or edited.
    """
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
