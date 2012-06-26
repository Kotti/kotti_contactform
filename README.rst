=================
kotti_contactform
=================

This is an extension to Kotti that allows to add a simple contact form
to your site.

`Find out more about Kotti`_

Development happens at https://github.com/chrneumann/kotti_contactform

Setup
=====

To enable the extension in your Kotti site, activate the configurator:

  kotti.configurators = kotti_contactform.kotti_configure

``kotti_contactform`` uses ``pyramid_mailer`` for sending mails and
tries to use your mailserver at localhost:25. If these defaults don't
fit your needs, you have to configure ``pyramid_mailer``:
http://packages.python.org/pyramid_mailer/

Database upgrade
================

If you upgrade from version 0.1.0 to 0.1.1 your database will be migrated
automatically. The migration is performed with `stucco_evolution`_. If you
have problems with the upgrade, please create a new issue in the `tracker`_.

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
.. _stucco_evolution: http://pypi.python.org/pypi/stucco_evolution
.. _tracker: https://github.com/chrneumann/kotti_contactform/issues
