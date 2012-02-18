=================
kotti_contactform
=================

This is an extension to Kotti that allows to add a simple contact form
to your site.

`Find out more about Kotti`_

Setup
=====

To enable the extension in your Kotti site, activate the configurator:

  kotti.configurators = kotti_contactform.kotti_configure

``kotti_contactform`` uses ``pyramid_mailer`` for sending mails and
tries to use your mailserver at localhost:25. If these defaults don't
fit your needs, you have to configure ``pyramid_mailer``:
http://packages.python.org/pyramid_mailer/

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
