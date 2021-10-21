import click
import logging

from ..logger import admin_logger
from . import _scan_groups_and_users
from . import _print_used_id_ranges
from . import _print_unused_id_ranges

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