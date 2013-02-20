from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from .settings import UID_MAX_LENGTH
from .utils import generate_uid


class Bookmark(models.Model):
    """
    Bookmark model.
    """
    user = models.ForeignKey(
        'auth.User', related_name='bookmarks', verbose_name=_('user')
    )

    uid = models.CharField(
        _('UID'), max_length=UID_MAX_LENGTH, editable=False, unique=True
    )
    title = models.CharField(_('title'), max_length=64)
    url = models.URLField(_('URL'))

    description = models.TextField(
        _('description'), blank=True, validators=[MaxLengthValidator(1000)],
        help_text=_('You can use HTML for text markup. Max length: 1000 '
                    'symbols.')
    )

    class Meta:
        ordering = ('-pk', )
        unique_together = ('user', 'url')
        verbose_name = _('bookmark')
        verbose_name_plural = _('bookmarks')

    def __unicode__(self):
        """
        Unicode representation.
        """
        return self.title

    def get_absolute_url(self):
        """
        Bookmark opens it URL in search.
        """
        return self.url


@receiver(signals.pre_save, sender=Bookmark)
def auto_uid_and_validate(instance, **kwargs):
    """
    Generate bookmark UID if necessary and then run validation.
    """
    # First check if no UID stored to bookmark - generate a new one
    if not instance.uid:
        while True:
            uid = generate_uid()

            try:
                Bookmark.objects.get(uid=uid)
            except Bookmark.DoesNotExist:
                instance.uid = uid
                break

    # Now run full validation
    instance.full_clean()
