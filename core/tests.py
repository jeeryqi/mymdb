from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse
from django.contrib.auth.models import AnonymousUser, User

from .models import Movie
from .views import MovieList


# Create your tests here.

class MovieListPaginationTestCase(TestCase):
    ACTIVE_PAGINATION_HTML = '''
    <li class="page-item active">
        <a href="{}?page={}" class="page-link">{}</a>
    </li>
    '''

    def setUp(self):
        for n in range(15):
            Movie.objects.create(
                title='Title {}'.format(n),
                plot='Plot {}'.format(n),
                year=1990 + n,
                rating=0,
                runtime=100 + n,
            )
        # User.objects.create_user(username='admin1', email='admin1@admin1.com', password='rootroot')

    def testFirstPage(self):
        movie_list_path = reverse('core:MovieList')
        request = RequestFactory().get(path=movie_list_path)
        response = MovieList.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(
                movie_list_path, 1, 1
            ),
            response.rendered_content
        )
