# -*- coding: utf-8 -*-

"""Configure your GitHub repository from a file, without having to click around in the UI."""

from __future__ import absolute_import, division, print_function

from setuptools import find_packages, setup


url = 'https://github.com/jacquerie/github-file'

readme = open('README.rst').read()

setup_requires = [
    'autosemver~=0.0,>=0.5.3',
]

install_requires = [
    'click~=6.0,>=6.7',
    'github3.py~=1.0,>=1.1.0',
    'python-dotenv~=0.0,>=0.8.2',
    'six~=1.0,>=1.11.0',
]

docs_require = []

tests_require = [
    'flake8-future-import~=0.0,>=0.4.4',
    'pytest-cov~=2.0,>=2.5.1',
    'pytest-vcr~=0.0,>=0.3.0',
    'pytest~=3.0,>=3.2.3',
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name not in ['all']:
        extras_require['all'].extend(reqs)

packages = find_packages(exclude=['docs', 'tests'])

setup(
    name='github-file',
    autosemver={
        'bugtracker_url': url + '/issues',
    },
    url=url,
    license='MIT',
    author='Jacopo Notarstefano',
    author_email='jacopo.notarstefano@gmail.com',
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    description=__doc__,
    long_description=readme,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'github-file = github_file.cli:cli',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
