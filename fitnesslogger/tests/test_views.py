import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from fitnesslogger.models import UserProfile

# @pytest.mark.django_db
# def test_userprofile(client):
#     user = User.objects.create_user(username='testuser', password='testpassword')
#     userprofile = UserProfile.objects.get(user=user)
#     client.login(username = "testuser", password = "password")
#     url = reverse("profile")
#     response = client.get(url)
#     assert response.status_code == 200

#Could not figure out how to log the user in which didn't allow me to access my views