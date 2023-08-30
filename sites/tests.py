# from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APIClient
# from .models import Site
# from .serializers import Site_Serializer, SiteCompanySerializer

# class SiteViewTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_paginated_response(self):
#         url = reverse("site-list")
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue("results" in response.data)
#         self.assertEqual(response.data["results"], [])

#     def test_non_paginated_response(self):
#         url = reverse("site-list") + "?brief=true"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(isinstance(response.data, list))
#         self.assertEqual(len(response.data), 0)  # Assuming no data

#     def test_serializer_class(self):
#         url = reverse("site-list")
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data["results"], [])

#         url = reverse("site-list") + "?brief=true"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(isinstance(response.data, list))
#         self.assertEqual(len(response.data), 0)  # Assuming no data

#     def test_filtering(self):
#         # Create Site objects for testing
#         Site.objects.create(site_name="Site 1",)
#         Site.objects.create(site_name="Site 2",)
#         Site.objects.create(site_name="Site 3",)

#         url = reverse("site-list") + "?site_name=Site 1"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data["results"]), 1)
#         self.assertEqual(response.data["results"][0]["site_name"], "Site 1")

#         url = reverse("site-list") + "?brief=true&site_name=Site 2"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(isinstance(response.data, list))
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]["site_name"], "Site 2")
