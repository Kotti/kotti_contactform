from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='kotti_contactform',
      version=version,
      description="Simple contact form for Kotti sites",
      long_description="""\
This is an extension to Kotti that allows to add simple contact forms to your website.""",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: BSD License",
        ],
      keywords='kotti contact form',
      author='Christian Neumann',
      author_email='christian@datenkarussell.de',
      url='http://pypi.python.org/pypi/kotti_contactform',
      license='BSD License',
      packages=['kotti_contactform'],
      package_data={'kotti_contactform': ['templates/*.pt']},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'Kotti',
        'pyramid_mailer',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
