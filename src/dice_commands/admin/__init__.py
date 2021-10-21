import click
import click_completion
import click_completion.core
import logging

from ..logger import admin_logger
from . import _scan_groups_and_users
from . import _print_used_id_ranges
from . import _print_unused_id_ranges

click_completion.init()


@click.group()
@click.option('--debug/-d', is_flag=True)
@click.option('--verbose/-v', is_flag=True)
@click.pass_context
def dice_admin(ctx, debug, verbose):
    ctx.ensure_object(dict)
    # verbose is debug
    verbose = debug or verbose
    debug = verbose

    if debug:
        admin_logger.setLevel(logging.DEBUG)

    ctx.obj['DEBUG'] = debug
    ctx.obj['VERBOSE'] = verbose


@dice_admin.command()
@click.pass_context
def create_user(ctx):
    click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
    print("This is the create_user command")


@dice_admin.command()
def scan_groups_and_users():
    _scan_groups_and_users.main()


@dice_admin.command()
@click.argument("user_file")
@click.argument("group_file")
def print_used_id_ranges(user_file, group_file):
    _print_used_id_ranges.main(user_file, group_file)


@dice_admin.command()
@click.argument("user_file")
@click.argument("group_file")
def print_unused_id_ranges(user_file, group_file):
    _print_unused_id_ranges.main(user_file, group_file)

@dice_admin.command()
@click.option('--append/--overwrite', help="Append the completion code to the file", default=None)
@click.option('-i', '--case-insensitive/--no-case-insensitive', help="Case insensitive completion")
@click.argument('shell', required=False, type=click_completion.DocumentedChoice(click_completion.core.shells))
@click.argument('path', required=False)
def install(append, case_insensitive, shell, path):
    """Install the click-completion-command completion"""
    extra_env = {'_CLICK_COMPLETION_COMMAND_CASE_INSENSITIVE_COMPLETE': 'ON'} if case_insensitive else {}
    shell, path = click_completion.core.install(shell=shell, path=path, append=append, extra_env=extra_env)
    click.echo('%s completion installed in %s' % (shell, path))