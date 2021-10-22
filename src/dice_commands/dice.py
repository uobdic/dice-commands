import logging
from subprocess import call
from typing import Any
import typer

from . import admin
from . import benchmark
from . import docs
from . import job
from .logger import user_logger, admin_logger


def user_callback(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Debug output"),
):
    # verbose is debug
    verbose = debug or verbose
    debug = verbose

    if debug:
        user_logger.setLevel(logging.DEBUG)


def admin_callback(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Debug output"),
):
    # verbose is debug
    verbose = debug or verbose
    debug = verbose

    if debug:
        admin_logger.setLevel(logging.DEBUG)


app = typer.Typer()
app.add_typer(admin.app, name="admin", callback=admin_callback)
app.add_typer(benchmark.app, name="benchmark", callback=user_callback)
app.add_typer(docs.app, name="docs", callback=user_callback)
app.add_typer(job.app, name="job", callback=user_callback)


def main() -> Any:
    return app()
