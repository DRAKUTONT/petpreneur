import http
import random

import django.test
import django.urls
import parameterized


class StaticURLTests(django.test.TestCase):
    def test_redirect_to_login(self):
        response = django.test.Client().get(
            django.urls.reverse("jobs:create"),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.FOUND)
        response = django.test.Client().get(
            django.urls.reverse("jobs:edit", args=["01"]),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.FOUND)

    def test_jobs_url(self):
        response = django.test.Client().get(
            django.urls.reverse("jobs:jobs_list"),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    @parameterized.parameterized.expand(
        [
            ("0", http.HTTPStatus.FOUND),
            ("01", http.HTTPStatus.FOUND),
            ("010", http.HTTPStatus.FOUND),
            (10, http.HTTPStatus.FOUND),
            (100, http.HTTPStatus.FOUND),
            (random.randint(1, 100000), http.HTTPStatus.FOUND),
        ],
    )
    def test_jobs_deatail_positive_endpoint(self, value, status_code):
        response = django.test.Client().get(
            django.urls.reverse("jobs:detail", args=[value]),
        )
        self.assertEqual(response.status_code, status_code)

    @parameterized.parameterized.expand(
        [
            ("str",),
            ("1.1",),
            ("-0",),
            ("-987",),
            ("012qwerty",),
            ("qwer123qwer",),
            ("qwert5",),
            ("123qwe123",),
            ("123%",),
            ("0$",),
        ],
    )
    def test_jobs_deatail_negative_endpoint(self, value):
        with self.assertRaises(django.urls.exceptions.NoReverseMatch):
            django.test.Client().get(
                django.urls.reverse("jobs:detail", args=[value]),
            )


__all__ = []
