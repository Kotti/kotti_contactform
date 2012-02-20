from setuptools import setup, find_packages
from setuptools import Command
import sys, os

version = '0.1.0b'

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(name='kotti_contactform',
      version=version,
      description="Simple contact form for Kotti sites",
      long_description="""\
This is an extension to Kotti that allows to add simple contact forms to your website.""",
      classifiers=[
        "Development Status :: 4 - Beta",
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
      package_data={'kotti_contactform': ['templates/*.pt',
                                          'locale/*.*',
                                          'locale/*/LC_MESSAGES/*.*']},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'Kotti',
        'pyramid_mailer',
        'Babel',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      message_extractors = { "kotti_contactform": [
        ("**.py",   "chameleon_python", None ),
        ("**.pt",   "chameleon_xml", None ),
        ]},
      cmdclass = {'test': PyTest},
      )
