# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from github_file.cli import cli


def test_update_uses_the_provided_filename(runner):
    result = runner.invoke(cli, ['update', '-f', 'Githubfile'])

    assert 0 == result.exit_code
