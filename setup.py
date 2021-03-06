# This file was auto-generated by Shut. DO NOT EDIT
# For more information about Shut, check out https://pypi.org/project/shut/

from __future__ import print_function
import io
import os
import setuptools
import sys

readme_file = 'README.md'
if os.path.isfile(readme_file):
  with io.open(readme_file, encoding='utf8') as fp:
    long_description = fp.read()
else:
  print("warning: file \"{}\" does not exist.".format(readme_file), file=sys.stderr)
  long_description = None

requirements = [
  'requests >=2.22.0,<3.0.0',
  'beautifulsoup4 >=4.9.1,<5.0.0',
  'aiohttp >=3.6.2,<4.0.0',
  'click >=7.1.2,<8.0.0',
]

setuptools.setup(
  name = 'actnow-scrape',
  version = '0.0.0',
  author = 'Lukas Stevens',
  author_email = 'mail@lukas-stevens.de',
  description = 'Scrape data from the members of the European Parliament (MEPs) from the official EU websites.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lukasstevens/actnow-scrape',
  license = None,
  packages = setuptools.find_packages('src', ['test', 'test.*', 'tests', 'tests.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = True,
  install_requires = requirements,
  extras_require = {},
  tests_require = [],
  python_requires = '>=3.7.0,<4.0.0',
  data_files = [],
  entry_points = {
    'console_scripts': [
      'actnow-scrape = actnow_scrape.__main__:cli',
    ]
  },
  cmdclass = {},
  keywords = [],
  classifiers = [],
  zip_safe = True,
)
