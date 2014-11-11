=================
kotti_contactform
=================

This is an extension to Kotti that allows to add a simple contact form
to your site. |build status|_

`Find out more about Kotti`_

Development happens at https://github.com/Kotti/kotti_contactform

.. |build status| image:: https://secure.travis-ci.org/Kotti/kotti_contactform.png?branch=master
.. _build status: http://travis-ci.org/Kotti/kotti_contactform
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

Setup
=====

To enable the extension in your Kotti site, activate the configurator:

    kotti.configurators =
        kotti_settings.kotti_configure
        kotti_contactform.kotti_configure

Please note that ``kotti_contactform >= 0.4`` depends on kotti_settings_,
so you have to list it in your ``kotti.configurators`` too.

``kotti_contactform`` uses ``pyramid_mailer`` for sending mails and
tries to use your mailserver at localhost:25. If these defaults don't
fit your needs, you have to configure ``pyramid_mailer``:
http://packages.python.org/pyramid_mailer/

If you add kotti_contactform to an existing Kotti site (i.e. a Kotti
installation with an already existing database), you have to
initialize the database migration with Kotti's ``kotti-migrate``
console skript: ``kotti-migrate
stamp_head --scripts=kotti_contactform:alembic``.

Database upgrade
================

If you upgrade to version 0.1.1 or 0.4 you have to migrate your
database. The migration is performed with `alembic`_ and Kotti's
console script ``kotti-migrate``. To migrate, run ``kotti-migrate
upgrade_all --scripts=kotti_contactform:alembic``.

For integration of alembic in your environment please refer to the
`alembic documentation`_. If you have problems with the upgrade,
please create a new issue in the `tracker`_.

Settings
========

Point your browser to http://your.domain/@@settings to get to the settings page
or use the submenupoint of 'Site Setup'.

You can specify a default sender address that will be used as the default for newly created contact forms.

You can also enable the use of a captcha in your contact forms.
For the captcha the `reCAPTCHA`_ service is used.
You have to sign up to get a key pair in order to use the service on your site.
In the settings you have to save your public and your private key.
Have a look at https://developers.google.com/recaptcha/ to sign up and get your keys.


.. _alembic: http://pypi.python.org/pypi/alembic
.. _alembic documentation: http://alembic.readthedocs.org/en/latest/index.html
.. _tracker: https://github.com/chrneumann/kotti_contactform/issues
.. _kotti_settings: http://pypi.python.org/pypi/kotti_settings
.. _reCAPTCHA: https://developers.google.com/recaptcha/
