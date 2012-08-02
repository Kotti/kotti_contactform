=================
kotti_contactform
=================

This is an extension to Kotti that allows to add a simple contact form
to your site. |build status|_

`Find out more about Kotti`_

Development happens at https://github.com/chrneumann/kotti_contactform

.. |build status| image:: https://secure.travis-ci.org/chrneumann/kotti_contactform.png?branch=master
.. _build status: http://travis-ci.org/Pylons/Kotti
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

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

If you upgrade from version 0.1.0 to 0.1.1 you have to migrate your 
database. The migration is performed with `alembic`_. For the migration
you have to install alembic with::

  $ python setup.py install

or rerun your buildout. The migration is performed with::

  $ alembic -c development.ini upgrade head

For integration of alembic in your environment please refer to the 
`alembic documentation`_. If you have problems with the upgrade, 
please create a new issue in the `tracker`_.

.. _alembic: http://pypi.python.org/pypi/alembic
.. _alembic documentation: http://alembic.readthedocs.org/en/latest/index.html
.. _tracker: https://github.com/chrneumann/kotti_contactform/issues
