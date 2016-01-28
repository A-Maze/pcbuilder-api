import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, '../README.md')).read()

requires = [
    'pyramid',
    'WebError',
    'mongoengine',
    'jsonschema',
    'pyramid_debugtoolbar',
    'paste',
    'mongoengine']

test_requires = [
    'nose'
]

setup(name='api',
      version='0.0',
      description='api',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author="A-Maze",
      author_email='localhost@localhost.com',
      url='localhost',
      keywords='web pyramid pylons mongodb',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=test_requires,
      test_suite="api",
      entry_points = """\
      [paste.app_factory]
      main = api:main
      """,
      paster_plugins=['pyramid'],
      )
