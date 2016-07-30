#!/usr/bin/env python
# -*- coding: utf-8 -*-

from git_release import git_release

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [
	'clingon',
	'GitPython',
	'requests',
	'semver'
]

version = '0.0.1'  # TODO use git tag ;)

setup(
    name='git_release',
    version=version,
    description="github flow release",
    author="Antoine Desbordes",
    author_email='antoine.desbordes@gmail.com',
    url='https://github.com/CanalTP/git_release',
    packages=[
        'git_release',
    ],
    package_dir={'git_release': 'git_release'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='cli',
    classifiers=[
        # 'Development Status ::  3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={'console_scripts': [
        'git_release = git_release.git_release:git_release_script',
    ]},
)
