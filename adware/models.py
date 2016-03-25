import random

from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.utils.encoding import python_2_unicode_compatible

from . import utils as util
from . import defaults as defs

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


@python_2_unicode_compatible
class AdSense(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(
        AUTH_USER_MODEL,
        related_name="%(class)s",
        editable=False,
    )

    code = models.TextField(
        _("Adsense Code"),
        blank=True,
        null=True,
        help_text=_('Your Google "Responsive" Adsense Code.'),
    )

    ad_client = models.CharField(
        max_length=60,
        blank=True,
        null=True,
    )

    ad_slot = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    percentage = models.PositiveIntegerField(
        default=defs.ADWARE_MINIMUM_IMPRESSION_PERCENTAGE,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text=_('Ad impression percentage (1-100).'),
    )

    active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Active shows your ads.'),
    )

    suspended = models.BooleanField(
        _('suspended'),
        default=False,
        help_text=_('Suspended AdShare will not show ads. For admin use.'),
    )

    def __str__(self):
        return 'Adsense: {} [p:{}, a:{}]'.format(self.user.username, self.percentage, self.active)

    def get_info(self):
        """
        Returns ad client/slot or None
        """
        if not self.user.is_active or not self.is_active or self.is_suspended:
            return None

        if not self.code or not self.ad_client or not self.ad_slot:
            return None

        rand = random.randint(1, 100)
        if rand > self.percentage:
            return None

        return self.ad_client, self.ad_slot
