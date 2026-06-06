from http import HTTPStatus

from django.test import TestCase

from app_utils.testdata_factories import UserMainFactory


class TestViews(TestCase):
    def test_should_show_index_view(self):
        # given
        user = UserMainFactory(permissions__=["example.basic_access"])
        self.client.force_login(user)

        # when
        response = self.client.get("/example/")

        # then
        self.assertEqual(response.status_code, HTTPStatus.OK)
