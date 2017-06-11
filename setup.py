#!/usr/bin/python

from setuptools import setup, find_packages
import medium

setup(name='medium',
      version='0.1-dev',
      description='Save medium posts right to your databse!',
      author='Vinay Khobragade',
      author_email='vinaykhobragade2016@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'medium = medium.medium:main',
            ]
      },
      include_package_data=True,
      url='https://www.github.com/feat7/medium-scraper',
      keywords=['medium', 'terminal', 'command-line', 'scraper', 'python', 'sqlite'],
      license='MIT',
      classifiers=[],
      install_requires=[
            'selenium',
            'BeautifulSoup4',
            'bleach',
      ]
     )