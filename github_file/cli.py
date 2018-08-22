# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

import click
from dotenv import find_dotenv, load_dotenv
from github3 import GitHub
from six.moves import configparser

DEFAULT_FILENAME = os.path.join('.github', 'Githubfile')

DEFAULT_LABELS = [
    {
        'name': 'bug',
        'color': '#d73a4a',
        'description': 'Something isn\'t working',
    },
    {
        'name': 'duplicate',
        'color': '#cfd3d7',
        'description': 'This issue or pull request already exists',
    },
    {
        'name': 'enhancement',
        'color': '#a2eeef',
        'description': 'New feature or request',
    },
    {
        'name': 'good first issue',
        'color': '#7057ff',
        'description': 'Good for newcomers',
    },
    {
        'name': 'help wanted',
        'color': '#008672',
        'description': 'Extra attention is needed',
    },
    {
        'name': 'invalid',
        'color': '#e4e669',
        'description': 'This doesn\'t seem right',
    },
    {
        'name': 'question',
        'color': '#d876e3',
        'description': 'Further information is requested',
    },
    {
        'name': 'wontfix',
        'color': '#ffffff',
        'description': 'This will not be worked on',
    },
]


@click.group()
@click.version_option()
def cli():
    load_dotenv(find_dotenv(usecwd=True))


@cli.command()
@click.option('-f', '--file', 'filename', default=DEFAULT_FILENAME)
def update(filename):
    """Update the repo to match the config file."""
    parser = configparser.ConfigParser()
    parser.read(filename)

    owner = parser.get('core', 'owner')
    repo = parser.get('core', 'repo')

    description = ''
    if parser.has_option('core', 'description'):
        description = ' '.join(parser.get('core', 'description').split())
    homepage = ''
    if parser.has_option('core', 'homepage'):
        homepage = parser.get('core', 'homepage')
    private = False
    if parser.has_option('core', 'private'):
        private = parser.getboolean('core', 'private')
    topics = []
    if parser.has_option('core', 'topics'):
        topics = parser.get('core', 'topics').split(', ')

    has_issues = True
    if parser.has_option('features', 'has_issues'):
        has_issues = parser.getboolean('features', 'has_issues')
    has_projects = True
    if parser.has_option('features', 'has_projects'):
        has_projects = parser.getboolean('features', 'has_projects')
    has_wiki = True
    if parser.has_option('features', 'has_wiki'):
        has_wiki = parser.getboolean('features', 'has_wiki')

    labels = DEFAULT_LABELS
    if parser.has_option('issues', 'labels'):
        labels = []
        for line in parser.get('issues', 'labels').split('\n'):
            labels.append(_parse_label(line))

    allow_squash_merge = True
    if parser.has_option('merges', 'allow_squash_merge'):
        allow_squash_merge = parser.getboolean('merges', 'allow_squash_merge')
    allow_merge_commit = True
    if parser.has_option('merges', 'allow_merge_commit'):
        allow_merge_commit = parser.getboolean('merges', 'allow_merge_commit')
    allow_rebase_merge = True
    if parser.has_option('merges', 'allow_rebase_merge'):
        allow_rebase_merge = parser.getboolean('merges', 'allow_rebase_merge')

    config = {
        'description': description,
        'homepage': homepage,
        'private': private,
        'has_issues': has_issues,
        'has_projects': has_projects,
        'has_wiki': has_wiki,
        'allow_squash_merge': allow_squash_merge,
        'allow_merge_commit': allow_merge_commit,
        'allow_rebase_merge': allow_rebase_merge,
    }

    github_user = os.getenv('GITHUB_USER')
    github_pass = os.getenv('GITHUB_PASS')
    github = GitHub(github_user, github_pass)

    repository = github.repository(owner, repo)
    repository.edit(repo, **config)
    repository.replace_topics(topics)
    for label in repository.labels():
        label.delete()
    for label in labels:
        repository.create_label(**label)


def _parse_label(line):
    parts = line.split(', ')
    if len(parts) == 2:
        name, color = parts
        return {'name': name, 'color': color}
    elif len(parts) == 3:
        name, color, description = parts
        return {'name': name, 'color': color, 'description': description}
