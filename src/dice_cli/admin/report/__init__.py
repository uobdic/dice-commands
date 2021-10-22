from typing import List
import logging
import typer

from dice_cli.logger import admin_logger


app = typer.Typer(help="Commands for report creation")


@app.command()
def storage(paths: List[str] = typer.Argument(...)) -> None:
    admin_logger.warning("Not implemented yet")
    for path in paths:
        admin_logger.info(f"Creating report for storage {path}")

