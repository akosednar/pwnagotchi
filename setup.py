#!/usr/bin/env python3
from setuptools import setup, find_packages
import pwnagotchi

required = []
with open('requirements.txt') as fp:
    for line in fp:
        line = line.strip()
        if line != "":
            required.append(line)

setup(name='pwnagotchi',
      version=pwnagotchi.version,
      description='Pwnagotchi is a cute AI that eats WPA handshakes.',
      author='evilsocket && the dev team',
      author_email='evilsocket@gmail.com',
      url='https://pwnagotchi.ai/',
      install_requires=required,
      scripts=['bin/pwnagotchi'],
      license='GPL',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Environment :: Console',
      ])