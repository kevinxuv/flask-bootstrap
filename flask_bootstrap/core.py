# -*- coding: utf-8 -*-
import os
import shutil

import git
from jinja2 import Environment, FileSystemLoader

from flask_bootstrap import current_path
from flask_bootstrap.exc import DirectoryAlreadyExist

env = Environment(loader=FileSystemLoader(current_path + '/templates'))


def render_template(template: str, **kwargs) -> bytes:
    return env.get_template(template).render(**kwargs).encode()


def bootstrap_project_dir(
        project_root_dir: str,
        project_name: str,
        project_description: str):
    if os.path.exists(project_root_dir):
        shutil.rmtree(project_root_dir)
    project_package_dir = project_root_dir + '/{}'.format(project_name)
    os.makedirs(project_package_dir)
    with open(project_package_dir + '/__init__.py', 'wb') as fh:
        fh.write(env.get_template('__init__.py.jinja').render().encode())
    with open(project_root_dir + '/README.md', 'wb') as fh:
        fh.write(render_template(
            'README.md.jinja',
            project_name=project_name,
            description=project_description)
        )
    with open(f'{project_package_dir}/settings.py', 'wb') as fh:
        fh.write(render_template('settings.py.jinja', project_name=project_name))
    with open(f'{project_package_dir}/wsgi.py', 'wb') as fh:
        fh.write(render_template('wsgi.py.jinja', project_name=project_name))


def bootstrap_project_git_dir(project_root_dir):
    git.Repo.init(project_root_dir)
    with open(project_root_dir + '/.gitignore', 'wb') as fh:
        fh.write(env.get_template('gitignore.jinja').render().encode())


def bootstrap(name: str = 'unknown', description: str = 'none', init_git: bool = False) -> str:
    project_root_dir = os.path.join(os.getcwd(), f'{name}')
    try:
        if os.path.exists(project_root_dir):
            raise DirectoryAlreadyExist(f'project directory already exist: {project_root_dir}')
        bootstrap_project_dir(project_root_dir, name, description)
        if init_git:
            bootstrap_project_git_dir(project_root_dir)
        return project_root_dir
    except DirectoryAlreadyExist:
        raise
    except Exception:
        if os.path.exists(project_root_dir):
            shutil.rmtree(project_root_dir)
        raise
