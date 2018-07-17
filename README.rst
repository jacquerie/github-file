=============
 GitHub-File
=============

.. image:: https://travis-ci.org/jacquerie/github-file.svg?branch=master
    :target: https://travis-ci.org/jacquerie/github-file

.. image:: https://coveralls.io/repos/github/jacquerie/github-file/badge.svg?branch=master
    :target: https://coveralls.io/github/jacquerie/github-file?branch=master


About
=====

Configure your GitHub repository from a file, without having to click around in
the UI.


Install
=======

``github-file`` is on PyPI, so all you have to do is:

.. code-block:: console

    $ pip install github-file


Usage
=====

First, you will need to provide your GitHub credentials through the
environment.  Since ``github-file`` uses ``python-dotenv`` you can do so by
creating a ``.env`` file with the following contents:

.. code-block:: shell

    GITHUB_USER=your_username
    GITHUB_PASS=your_password

Next, you will need to create a valid ``Githubfile``. Here's an example of one:

.. code-block:: ini

    [core]
    owner = jacquerie
    repo = github-file
    description = Configure your GitHub repository from a file,
        without having to click around in the UI.
    topics = github, configuration, file

    [features]
    has_issues = true
    has_projects = false
    has_wiki = false

    [merges]
    allow_squash_merge = false
    allow_merge_commit = false
    allow_rebase_merge = true

The meaning of these options is explained in `GitHub's API documentation`_,
although not all the options are currently supported (in particular you
currently can't archive the repository or configure the default branch.)

Finally, running

.. code-block:: console

    $ github-file update -f Githubfile

will update the configuration of your GitHub repository so that it matches what
is described in the file. Note that if you don't provide a filename it will
look by default in ``.github/Githubfile``.

.. _`GitHub's API documentation`: https://developer.github.com/v3/repos/#edit


Author
======

Jacopo Notarstefano (`@Jaconotar`_)

.. _`@Jaconotar`: https://twitter.com/Jaconotar


License
=======

MIT
