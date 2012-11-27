from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

install_requires = [
    'Kotti >= 0.8a1',
    'Babel',
    'Pillow',
    'colander >= 0.9.8',
    'alembic',
]

setup(name='kotti_contactform',
      version='0.1.1dev',
      description="Simple contact form for Kotti sites",
      long_description=README + '\n\n' + CHANGES,
      keywords='kotti contact form',
      maintainer='Christian Neumann',
      maintainer_email='cneumann@datenkarussell.de',
      url='http://pypi.python.org/pypi/kotti_contactform',
      classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: BSD License",
        ],
      author='Christian Neumann and contributors',
      author_email='cneumann@datenkarussell.de',
      license='BSD-2-Clause',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={},
      message_extractors={"kotti_events": [
        ("**.py", "lingua_python", None),
        ("**.pt", "lingua_xml", None),
        ]},
      )
