import os
from pathlib import Path
from typing import List, Optional

import typer

from dice_cli.logger import admin_logger
from dice_cli.utils import convert_to_largest_unit

app = typer.Typer(help="Commands for report creation")


@app.command()
def storage(
    paths: List[Path] = typer.Argument(...),
    output_directory: Optional[Path] = typer.Option(
        "--output", "-o", help="Output directory"
    ),
) -> None:
    admin_logger.warning(":construction: Work in progress :construction:")
    for path in paths:
        admin_logger.info(f"Creating report for storage {path}")
        total = sum(
            os.stat(item).st_size for item in path.glob("**/*") if os.path.exists(item)
        )
        total_scaled, unit = convert_to_largest_unit(total, "B", scale=1024)
        admin_logger.info(f"{total_scaled = :.2f} {unit}")
