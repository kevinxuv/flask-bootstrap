# -*- coding: utf-8 -*-
import logging

import click

from flask_bootstrap.core import bootstrap


logger = logging.getLogger(__name__)


@click.command()
def cli():
    name = click.prompt(
        '-> Give your flask project a name', default='unknown', type=str)
    description = click.prompt(
        '-> Give a description for your flask project', default='none', type=str)
    init_git = click.prompt('-> Init git or not?', default=False, type=bool)
    # venv = click.prompt('-> create virtualenv or not?', default=False, type=bool)
    click.echo(click.style(f'Start to bootstrap project {name}...', fg='blue', bold=True))
    try:
        project_root_dir = bootstrap(name=name, description=description, init_git=init_git)
        click.echo(
            click.style(
                f'Finish bootstrap project {name} at {project_root_dir}',
                fg='blue',
                bold=True
            )
        )
    except Exception as e:
        logger.exception(e)
        click.echo(click.style(f'[ERROR] failed to bootstrap project: {e}', fg='red', bold=True))


if __name__ == '__main__':
    cli()
