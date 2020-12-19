from django.db import models
import uuid

from django.forms import model_to_dict

import random
import string


class ModelDiffMixin(object):
    """
    Mixin that detects changes in model fields.
    """

    def __init__(self, *args, **kwargs):
        super(ModelDiffMixin, self).__init__(*args, **kwargs)
        self.__initial = self._dict

    @property
    def diff(self):
        d1 = self.__initial
        d2 = self._dict
        diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
        return dict(diffs)

    @property
    def has_changed(self):
        return bool(self.diff)

    @property
    def changed_fields(self):
        return self.diff.keys()

    def get_field_diff(self, field_name):
        """
        Returns a diff for field if it's changed and None otherwise.
        """
        return self.diff.get(field_name, None)

    def save(self, *args, **kwargs):
        """
        Saves model and set initial state.
        """
        super(ModelDiffMixin, self).save(*args, **kwargs)
        self.__initial = self._dict

    @property
    def _dict(self):
        return model_to_dict(self, fields=[field.name for field in
                                           self._meta.fields])


class Link(models.Model, ModelDiffMixin):
    initial_link = models.URLField(verbose_name="Link to redirect")
    truncated_link_uuid = models.CharField(max_length=10,
                                           unique=True,
                                           db_index=True,
                                           editable=False)
    created = models.DateTimeField(auto_now=True)

    @property
    def truncated_link(self):
        return 'http://localhost:8080/' + self.truncated_link_uuid

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        letters = string.ascii_letters
        self.truncated_link_uuid = ''.join(random.choice(letters) for _ in range(10))
        super().save()

    class Meta:
        verbose_name = "Link"
        ordering = ('-created', )
