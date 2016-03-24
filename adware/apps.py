from django.db.models import signals
from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    """
    Configuration entry point for the adware app
    """
    label = name = 'adware'
    verbose_name = "adware"

    def ready(self):
        """
        App is imported and ready, so bootstrap it.
        """
        from django.contrib.auth import get_user_model
        from . import receivers as rcv

        User = get_user_model()
        signals.post_save.connect(rcv.create_ad, sender=User)
