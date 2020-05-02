from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.utils import json

from photos.models import Photo
from photos.serializers import PhotoSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_photo(user="", caption=""):
        if user != "" and caption != "":
            Photo.objects.create() .objects.create(user=user, caption=caption)

    def setUp(self):
        # create a admin user
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test@mail.com",
            password="testing",
            first_name="test",
            last_name="user",
        )
        # add test data
        self.create_photo("user1", "image1")
        self.create_photo("user1", "image2")
        self.create_photo("admin", "image3")
        self.create_photo("admin", "image4")


class GetAllPostsTest(BaseViewTest):

    def test_get_all_pics(self):
        """
        This test ensures that all posts added in the setUp method
        exist when we make a GET request to the photos/ endpoint
        """
        self.login_client('test_user', 'testing')
        # hit the API endpoint
        response = self.client.get(
            reverse("photos")
        )
        # fetch the data from db
        expected = Photo.objects.all()
        serialized = PhotoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)