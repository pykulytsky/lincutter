from django.db import models
import uuid


class Link(models.Model):
    initial_link = models.URLField(verbose_name="Link to redirect")
    truncated_link_uuid = models.UUIDField(default=uuid.uuid4(), max_length=10)
    created = models.DateTimeField(auto_now=True)

    @property
    def truncated_link(self):
        return 'http://' + self.truncated_link_uuid

    class Meta:
        verbose_name = "Link"
        ordering = '-created'
