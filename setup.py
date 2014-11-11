import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

install_requires = [
    'alembic',
    'Babel',
    'colander >= 0.9.8',
    'httplib2',
    'Kotti >= 0.9.2',
    'kotti_settings',
    'Pillow',
]


setup(name='kotti_contactform',
      version='0.5dev',
      description="Simple contact form for Kotti sites",
      long_description=README + '\n\n' + CHANGES,
      keywords='kotti contact form',
      maintainer='Kotti developers',
      maintainer_email='kotti@googlegroups.com',
      url='https://github.com/Kotti/kotti_contactform',
      classifiers=[
          "Development Status :: 4 - Beta",
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "License :: OSI Approved :: BSD License",
      ],
      author='Kotti developers',
      author_email='kotti@googlegroups.com',
      license='BSD-2-Clause',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={},
      message_extractors={"kotti_contactform": [
          ("**.py", "lingua_python", None),
          ("**.pt", "lingua_xml", None),
      ]},
      )
