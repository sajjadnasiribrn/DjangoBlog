from django.contrib.sitemaps import Sitemap
from blog.models import Post, Category
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, item):
        return reverse('blog:show-post', kwargs={'slug': item.slug, 'pid': item.id})


class CategoriesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, item):
        return reverse('blog:show-category-posts', kwargs={'slug': item.slug, 'cid': item.id})
