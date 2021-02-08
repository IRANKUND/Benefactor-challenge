# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in benefactor_challenge/__init__.py
from benefactor_challenge import __version__ as version

setup(
	name='benefactor_challenge',
	version=version,
	description='this app is a challenge to take in order to have clear understanding of frappe',
	author='patrick',
	author_email='patrick@info.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
