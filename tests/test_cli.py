# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest

from github_file.cli import cli

GITHUB_FILE = '''\
[core]
owner = jacquerie
repo = github-file
description = Configure your GitHub repository from a file,
    without having to click around in the UI.

[features]
has_issues = true
has_projects = false
has_wiki = false

[merges]
allow_squash_merge = false
allow_merge_commit = false
allow_rebase_merge = true
'''


@pytest.mark.vcr()
def test_update_uses_the_provided_filename(runner, tmpdir):
    config_fd = tmpdir.join('Githubfile')
    config_fd.write(GITHUB_FILE)

    result = runner.invoke(cli, ['update', '-f', str(config_fd)])

    assert 0 == result.exit_code
