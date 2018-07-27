# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from textwrap import dedent

import pytest

from github_file.cli import cli


@pytest.mark.vcr()
def test_update_can_set_the_description(runner, tmpdir):
    config_fd = tmpdir.join('Githubfile')
    config_fd.write(dedent(u'''\
    [core]
    owner = jacquerie
    repo = github-file
    description = Configure your GitHub repository from a file,
        without having to click around in the UI.
    '''))

    result = runner.invoke(cli, ['update', '-f', str(config_fd)])

    assert 0 == result.exit_code


@pytest.mark.vcr()
def test_update_can_set_the_topics(runner, tmpdir):
    config_fd = tmpdir.join('Githubfile')
    config_fd.write(dedent(u'''\
    [core]
    owner = jacquerie
    repo = github-file
    topics = github, configuration, file
    '''))

    result = runner.invoke(cli, ['update', '-f', str(config_fd)])

    assert 0 == result.exit_code


@pytest.mark.vcr()
def test_update_can_configure_which_features_to_use(runner, tmpdir):
    config_fd = tmpdir.join('Githubfile')
    config_fd.write(dedent(u'''\
    [core]
    owner = jacquerie
    repo = github-file

    [features]
    has_issues = true
    has_projects = false
    has_wiki = false
    '''))

    result = runner.invoke(cli, ['update', '-f', str(config_fd)])

    assert 0 == result.exit_code


@pytest.mark.vcr()
def test_update_can_configure_the_issue_labels(runner, tmpdir):
    config_fd = tmpdir.join('Githubfile')
    config_fd.write(dedent(u'''\
    [core]
    owner = jacquerie
    repo = github-file

    [issues]
    labels = enhancement, #a2eeef
        bug, #d73a4a
        question, #d876e3
    '''))

    result = runner.invoke(cli, ['update', '-f', str(config_fd)])

    assert 0 == result.exit_code


@pytest.mark.vcr()
def test_update_can_configure_the_merge_policy(runner, tmpdir):
    config_fd = tmpdir.join('Githubfile')
    config_fd.write(dedent(u'''\
    [core]
    owner = jacquerie
    repo = github-file

    [merges]
    allow_squash_merge = false
    allow_merge_commit = false
    allow_rebase_merge = true
    '''))

    result = runner.invoke(cli, ['update', '-f', str(config_fd)])

    assert 0 == result.exit_code
