import logging
from typing import Any, Optional

import rich
import typer

from . import __version__, _date, benchmark, check, docs, info, job
from .logger import console_handler, user_logger


def user_callback(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Debug output"),
) -> Any:
    # verbose is debug
    verbose = debug or verbose
    debug = verbose

    if debug:
        user_logger.setLevel(logging.DEBUG)
        # workaround for rich
        console_handler.setLevel(logging.DEBUG)


app = typer.Typer()
app.add_typer(benchmark.app, name="benchmark", callback=user_callback)
app.add_typer(check.app, name="check", callback=user_callback)
app.add_typer(docs.app, name="docs", callback=user_callback)
app.add_typer(info.app, name="info", callback=user_callback)
app.add_typer(job.app, name="job", callback=user_callback)


@app.command()
def version() -> None:
    """
    Show version
    """
    rich.print(f"[blue]DICE CLI Version[/]: [magenta]{__version__}[/]")


@app.command()
def glossary(
    word: Optional[str] = typer.Argument(None, help="Word to search for"),
    print_all: bool = typer.Option(
        False, "--all", "-a", help="Print all glossary entries"
    ),
) -> None:
    """
    Show the meaning of a given word (in DICE context)
    """
    from dice_lib import GLOSSARY

    if print_all:
        from prettytable import PrettyTable

        x = PrettyTable()
        x.field_names = ["Word", "Meaning"]
        for word, meaning in GLOSSARY.items():
            x.add_row([word, meaning])
        x.align = "l"
        rich.print(x)
        return

    if word not in GLOSSARY:
        rich.print(f"[red]Word '{word}' not found[/]")
        typer.echo("To list all glossary items use 'dice glossary -a'")
        return

    rich.print(f"[blue]{word}[/]: [magenta]{GLOSSARY[word]}[/]")


@app.command()
def date(
    date_format: _date.DateOptions = typer.Option(
        _date.DateOptions.ISO8601_JUST_Y_M_D,
        "--format",
        "-f",
        help="Format to print",
        case_sensitive=False,
    )
) -> None:
    """
    Print the current date in ISO8601 format
    """
    rich.print(_date.formatted_date(date_format))


@app.command()
def contribute() -> None:
    """
    Contribute to DICE
    """
    rich.print("[blue]Contribute[/]:")
    rich.print("[blue]  DICE CLI[/]: [red]https://github.com/uobdic/dice-cli[/]")
    rich.print("[blue]  DICE LIB[/]: [red]https://github.com/uobdic/dice-lib[/]")
    rich.print("[blue]  DICE WIKI[/]: [red]https://wikis.bris.ac.uk/display/dic[/]")


def main() -> Any:
    return app()
