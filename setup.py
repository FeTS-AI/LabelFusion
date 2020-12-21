#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
  readme = readme_file.read()

requirements = [
  'numpy==1.19.3',
  'SimpleITK==1.2.4',
  'setuptools',
  'wheel',
  'twine',
  'keyring',
  'artifacts-keyring'
]

setup(
  name='LabelFusion',
  version='0.0.2.NR', # NR: non-release; this should be changed when tagging\
  author="Megh Bhalerao, Sarthak Pati",
  author_email='software@cbica.upenn.edu',
  python_requires='>=3.6',
  scripts=['fusion_run'],
  classifiers=[
    'Development Status :: Pre-Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD-3-Clause License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  description=(
    "Label fusion strategies for multi-class labels."
  ),
  install_requires=requirements,
  license="BSD-3-Clause License",
  long_description=readme,
  long_description_content_type='text/markdown',
  include_package_data=True,
  keywords='semantic, segmentation, brain, breast, liver, lung, label-fusion, fusion',
  zip_safe=False,
)
