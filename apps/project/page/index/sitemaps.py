from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class IndexViewSitemap(Sitemap):
    
    def items(self):
        return ['index:home']
    
    def location(self, item):
        return reverse(item)