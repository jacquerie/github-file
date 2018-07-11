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

Currently ``github-file`` implements one subcommand:

.. code-block:: console

    $ github-file update

This will update the configuration of your repository on GitHub so that it
matches what is described in a file called (by default) ``Githubfile`` in the
``.github`` folder.


Author
======

Jacopo Notarstefano (`@Jaconotar`_)

.. _`@Jaconotar`: https://twitter.com/Jaconotar


License
=======

MIT
