from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    # priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['website:home', 'website:contact']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return {'website:home': 1.0, 'website:contact': 0.8}[item]
