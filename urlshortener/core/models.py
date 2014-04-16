from django.db import models
from django.contrib.sites.models import Site

from .utils import random_text


class Link(models.Model):

    url = models.URLField('Link')
    slug = models.SlugField('Slug')
    views = models.IntegerField('Views Count', default=0, blank=True)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = random_text()
            while Link.objects.filter(slug=slug).exists():
                slug = random_text()
            self.slug = slug
        return super(Link, self).save(*args, **kwargs)

    def get_short_url(self):
        site = Site.objects.get_current()
        return 'http://%s/%s' % (site.domain, self.slug)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['-created_at']
