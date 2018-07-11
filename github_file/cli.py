# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

import click

DEFAULT_FILENAME = os.path.join('.github', 'Githubfile')


@click.group()
@click.version_option()
def cli():
    pass


@cli.command()
@click.option('-f', '--file', 'filename', default=DEFAULT_FILENAME)
def update(filename):
    """Update the repo to match the config file."""
