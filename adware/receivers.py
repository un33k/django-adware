from . models import AdSense


def create_ad(sender, instance, created, *args, **kwargs):
    """
    Create an ad object upon profile creation.
    """
    created = False
    try:
        obj = AdSense.objects.get(profile=instance)
    except AdSense.DoesNotExist:
        try:
            with transaction.atomic():
                obj = AdSense.objects.create(profile=instance)
                created = True
        except IntegrityError:
            obj = AdSense.objects.get(profile=instance)
