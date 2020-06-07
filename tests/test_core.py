import os
import tempfile
import shutil

import pytest


from flask_bootstrap.core import (bootstrap_project_dir, bootstrap_project_git_dir, bootstrap)


@pytest.fixture()
def tmp_dir():
    _tmp_dir = tempfile.mkdtemp()
    yield _tmp_dir
    print('start to teardown...')
    shutil.rmtree(_tmp_dir)


@pytest.fixture()
def project_name():
    return 'test'


@pytest.fixture()
def project_description():
    return 'test'


def test_bootstrap_project_dir(tmp_dir, project_name, project_description):
    bootstrap_project_dir(tmp_dir, project_name, project_description)
    assert os.path.exists(f'{tmp_dir}') is True
    assert os.path.exists(f'{tmp_dir}/README.md') is True
    assert os.path.exists(f'{tmp_dir}/{project_name}/wsgi.py') is True
    assert os.path.exists(f'{tmp_dir}/{project_name}/settings.py') is True
    assert os.path.exists(f'{tmp_dir}/{project_name}/__init__.py') is True


def test_bootstrap_project_git_dir(tmp_dir):
    bootstrap_project_git_dir(tmp_dir)
    assert os.path.exists(f'{tmp_dir}/.git') is True


def test_bootstrap(project_name, project_description):
    pwd = os.getcwd()
    tmp_dir = tempfile.mkdtemp()
    os.chdir(tmp_dir)
    project_root_dir = bootstrap(project_name, project_description, True)
    import platform
    if platform.system() == 'Darwin':
        tmp_dir = f'/private{tmp_dir}'
    assert project_root_dir == f'{tmp_dir}/{project_name}'
    assert os.path.exists(f'{project_root_dir}') is True
    assert os.path.exists(f'{project_root_dir}/README.md') is True
    assert os.path.exists(f'{project_root_dir}/{project_name}/wsgi.py') is True
    assert os.path.exists(f'{project_root_dir}/{project_name}/settings.py') is True
    assert os.path.exists(f'{project_root_dir}/{project_name}/__init__.py') is True
    shutil.rmtree(tmp_dir)
    os.chdir(pwd)
