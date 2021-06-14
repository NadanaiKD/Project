from my_profile.core.models import Email
from django.test import TestCase

from my_profile.core.models import Profile

# from core.model import


class TestProfile(TestCase):
    def test_profile_should_have_defined_filed(self):
        profile = Profile.objects.create(
            name="Moo",
            # github_url="",
            # facebook_url="",
            # twittwer_url="",
        )
        assert profile.name == "Moo"
        # assert profile.github_url == ""
        # assert profile.facebook_url == ""
        # assert profile.twitter_url == ""


class TestIndexView(TestCase):
    # def test_index_view_should_see_my_name(self):
    def test_index_view_should_be_accessible(self):
        # Given
        Profile.objects.create(name="Moo")

        # When
        response = self.client.get("/")

        # Then
        assert response.status_code == 200
        assert "Moo" in str(response.content)

    def test_index_view_should_save_subscriber_email_when_input_form(self):
        # Given
        Profile.objects.create(name="Moo")

        # When
        data = {
            "email": "Moo@testmail.com"
        }
        response = self.client.post("/", data=data)

        # then
        subscriber = Email.objects.last()
        assert response.status_code == 200
        assert subscriber.email == "Moo@testmail.com"


class SubscriberEmail(TestCase):
    def test_email_db_should_have_email_in_filed(self):
        # Given
        email = Email.objects.create(email="Moo@testemail.com",)
        # When

        # Then
        assert email.email == "Moo@testemail.com"


class ProjectAPIView(TestCase):
    def test_view_get_profile_should_be_accessible(self):

        response = self.client.get('/profile/')

        assert response.status_code == 200

    def test_view_get_profile_should_be_return_data(self):
        Profile.objects.create(
            name="moo",
        )
        expected = {
            "name": "moo",
        }

        response = self.client.get('/profile/')

        assert response.status_code == 200
        assert response.data["name"] == expected["name"]
