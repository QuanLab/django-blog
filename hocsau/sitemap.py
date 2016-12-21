from django.contrib.sitemaps import Sitemap
from models import Post


class JobPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def last_mod(self, obj):
        return obj.published_date