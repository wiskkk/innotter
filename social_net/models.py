from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=80)
    uuid = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField('innotter.Tag', related_name='pages')

    owner = models.ForeignKey('innotter.User', on_delete=models.CASCADE, related_name='pages')
    followers = models.ManyToManyField('innotter.User', related_name='follows')

    image = models.URLField(null=True, blank=True)

    is_private = models.BooleanField(default=False)
    follow_requests = models.ManyToManyField('innotter.User', related_name='requests')

    unblock_date = models.DateTimeField(null=True, blank=True)


class Post(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=180)

    reply_to = models.ForeignKey('innotter.Post', on_delete=models.SET_NULL, null=True, related_name='replies')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
