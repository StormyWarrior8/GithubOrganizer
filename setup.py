# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open

version = '0.1.0'

try:
    long_description = open('README.md').read()
except:
    long_description = ''


setup(

  name = 'githuborganizer',

  version = version,
  packages=find_packages(),

  description = '',
  long_description=long_description,
  long_description_content_type='text/markdown',
  python_requires='>=3',

  author = 'Robert Hafner',
  author_email = 'tedivm@tedivm.com',
  url = 'https://github.com/tedivm/githuborganizer',
  download_url = "https://github.com/tedivm/githuborganizer/archive/v%s.tar.gz" % (version),
  keywords = 'automation github organizations',

  classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',

    'Intended Audience :: Developers',
    'Topic :: Software Development :: Version Control',

    'Programming Language :: Python :: 3',
  ],

  install_requires=[
    'celery>=4.1,<5',
    'click>=7.0,<8.0',
    'cryptography>=2.1.4,<3',
    'github3.py>=1,<2',
    'github3apps.py>=0.1.3,<0.2',
    'pyjwt>=1.5.3,<2',
    'PyYAML>=5,<6',
    'fastapi==0.38.1',
  ],

  extras_require={
    'dev': [
      'pypandoc',
      'twine',
      'wheel'
    ],
  },
)
