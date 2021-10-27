from pathlib import Path
from typing import List, Optional

import typer
from dice_lib.date import current_formatted_date
from dice_lib.fs import size_of_paths

from dice_cli._io import write_list_data_to_csv
from dice_cli.logger import admin_logger

app = typer.Typer(help="Commands for report creation")


@app.command()
def storage(
    paths: List[Path] = typer.Argument(...),
    output_directory: Optional[Path] = typer.Option(
        None,
        "-o",
        "--output",
        help="Output directory",
    ),
) -> None:
    admin_logger.warning(":construction: Work in progress :construction:")

    headers = ["Path", "Size [B]", "Size [human-readable]", "Unit [human-readable]"]
    report = size_of_paths(paths)

    if not output_directory:
        today = current_formatted_date()
        output_directory = Path(f"/tmp/{today}_dice_admin_storage_report.csv")

    write_list_data_to_csv(report, headers, output_directory)
    admin_logger.info(f"Report saved to {output_directory}")
