from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

from .models import Link


class HomeViewTestCase(TestCase):

    def setUp(self):
        Link.objects.create(url='http://example.com', slug='example')
        self.client = Client()
        self.home_url = reverse('home')

    def tearDown(self):
        Link.objects.all().delete()

    def test_template_used(self):
        response = self.client.get(self.home_url)
        self.assertTemplateUsed(response, 'home.html')

    def test_form_error(self):
        initial_links = Link.objects.count()
        data = {
            'url': '',
            'slug': ''
        }
        response = self.client.post(self.home_url, data)
        current_links = Link.objects.count()
        self.assertEqual(initial_links, current_links)
        self.assertContains(response, 'required')
        data = {
            'url': '',
            'slug': 'example',
        }
        response = self.client.post(self.home_url, data)
        current_links = Link.objects.count()
        self.assertEqual(initial_links, current_links)
        self.assertContains(response, 'This slug already exists')

    def test_form_valid(self):
        data = {
            'url': 'http://test.com',
            'slug': 'test'
        }
        response = self.client.post(self.home_url, data)
        self.assertTrue(Link.objects.filter(slug='test').exists())


class RedirectViewTestCase(TestCase):

    def setUp(self):
        self.link = Link.objects.create(url='http://example.com', slug='example')
        self.client = Client()
        self.home_url = reverse('home')

    def tearDown(self):
        Link.objects.all().delete()

    def test_redirect(self):
        site = Site.objects.get_current()
        self.assertEqual(self.link.get_short_url(), 'http://%s/%s' % (site.domain, self.link.slug))
        response = self.client.get(reverse('link', args=['example']))
        self.assertRedirects(response, self.link.url)
