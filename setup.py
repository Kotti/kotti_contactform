import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
AUTHORS = open(os.path.join(here, 'AUTHORS.rst')).read()

install_requires = [
    'httplib2',
    'Kotti >= 0.10b1',
    'kotti_settings',
]


setup(name='kotti_contactform',
      version='0.6dev',
      description="Simple contact form for Kotti sites",
      long_description=README + '\n\n' + AUTHORS + '\n\n' + CHANGES,
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
