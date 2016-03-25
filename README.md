Django IPware
====================

**A Django application that enables profit sharing**

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]
[![download-image]][download-link]


Overview
====================

**Best attempt** to share AdSense profit while keeping it **DRY**.


How to install
====================

    1. easy_install django-adware
    2. pip install django-adware
    3. git clone http://github.com/un33k/django-adware
        a. cd django-adware
        b. run python setup.py
    4. wget https://github.com/un33k/django-adware/zipball/master
        a. unzip the downloaded file
        b. cd into django-adware-* directory
        c. run python setup.py


How to use
====================

   ```python
   # Add `adware` to your INSTALLED_APPS.
   # Run `manage.py migrate`.
   # In your settings.py set `ADWARE_TEMPLATE_BASE_DIR` to the directory for your template
   # Add `adware` to your urls.py - ex: url(r'^account/ads/', include('adware.urls', namespace='adware'))
   # `adense` & `form` will be passed to your template context for processing.
   ```

Running the tests
====================

To run the tests against the current environment:

    python manage.py test


License
====================

Released under a ([BSD](LICENSE.md)) license.


Version
====================
X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.

[status-image]: https://secure.travis-ci.org/un33k/django-adware.png?branch=master
[status-link]: http://travis-ci.org/un33k/django-adware?branch=master

[version-image]: https://img.shields.io/pypi/v/django-adware.svg
[version-link]: https://pypi.python.org/pypi/django-adware

[coverage-image]: https://coveralls.io/repos/un33k/django-adware/badge.svg
[coverage-link]: https://coveralls.io/r/un33k/django-adware

[download-image]: https://img.shields.io/pypi/dm/django-adware.svg
[download-link]: https://pypi.python.org/pypi/django-adware
