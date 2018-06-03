from django.conf.urls import url, include
from rest_framework import routers
from vegspotapi import views

app_name = 'app_v1'

router = routers.DefaultRouter()
router.register(r'users', views.PersonViewSet)
router.register(r'venues', views.VenueViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
