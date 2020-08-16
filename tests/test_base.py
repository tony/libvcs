# -*- coding: utf-8 -*-
"""tests for libvcs repo abstract base class."""
from __future__ import absolute_import, print_function, unicode_literals

from libvcs.base import BaseRepo, convert_pip_url
from libvcs.shortcuts import create_repo


def test_repr():
    repo = create_repo(url='file://path/to/myrepo', repo_dir='/hello/', vcs='git')

    str_repo = str(repo)
    assert 'GitRepo' in str_repo
    assert 'hello' in str_repo
    assert '<GitRepo hello>' == str_repo


def test_repr_base():
    repo = BaseRepo(url='file://path/to/myrepo', repo_dir='/hello/')

    str_repo = str(repo)
    assert 'Repo' in str_repo
    assert 'hello' in str_repo
    assert '<BaseRepo hello>' == str_repo


def test_ensure_dir_creates_parent_if_not_exist(tmpdir):
    parentdir = tmpdir.join('parentdir')  # doesn't exist yet
    repo_dir = parentdir.join('myrepo')
    repo = BaseRepo(url='file://path/to/myrepo', repo_dir=str(repo_dir))

    repo.ensure_dir()
    assert parentdir.check()


def test_convert_pip_url():
    url, rev = convert_pip_url(pip_url='git+file://path/to/myrepo@therev')

    assert url, rev == 'therev'
    assert url, rev == 'file://path/to/myrepo'
