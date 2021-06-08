from django.test import TestCase

from core.models import Profile

# from core.model import 



class TestProfile(TestCase):
    def test_profile_should_have_defined_filed(self):
        profile = Profile.objects.create(
            name="Moo",
            short_bio="LM is Me",
            github_url="",
            facebook_url="",
            twittwer_url="",
        )
        assert profile.name == "Moo"
        assert profile.short_bio == "LM is Me"
        assert profile.github_url == ""
        assert profile.facebook_url == ""
        assert profile.twitter_url == ""


class TestIndexView(TestCase):
    #def test_index_view_should_see_my_name(self):
    def test_index_view_should_be_accessible(self):
        #Given
        Profile.object.create(name="Moo")

        #When
        response = self.client.get("/")

        #Then
        assert response.status_code == 200
        assert "Moo" in str(response.content)

    def test_index_view_should_save_subscriber_email_when_input_form(self):
        #Given
        Profile.object.create(name="Moo")

        #When
        data = {
            "email" : "Moo@testmail.com"
        }
        response = self.client.post("/"), data=data)

        #then
        subscriber = Subscriber.object.last()
        assert subscriber.email == "Moo@testmail.com"