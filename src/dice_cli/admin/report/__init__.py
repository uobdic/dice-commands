from pathlib import Path
from typing import List, Optional, cast

import typer
from dice_lib.date import current_formatted_date
from tabulate import tabulate

from dice_cli._io import write_list_data_to_csv
from dice_cli.logger import admin_logger

from ._storage import generate_storage_report

app = typer.Typer(help="Commands for report creation")

# U = TypeVar("U")
# def optional_to_strict(optional: Optional[U]) -> U:
#     if optional is None:
#         raise ValueError("Value is None")
#     return cast(U, optional)


@app.command()
def storage(
    paths: List[Path] = typer.Argument(...),
    output_file: Optional[Path] = typer.Option(
        None,
        "-o",
        "--output",
        help="Output file",
    ),
    resolve_usernames: bool = typer.Option(False, "--resolve-usernames"),
    print_to_console: bool = typer.Option(
        False, "--print", help="Print to console instead of output file"
    ),
) -> None:
    """
    Generate a report of the storage usage of the given paths.

    :param paths: The paths to generate the report for.
    :param output_directory: The directory to write the report to.
    :param resolve_usernames: Whether to resolve usernames to their real names.
    """
    if not output_file and not print_to_console:
        today = current_formatted_date()
        output_file = Path(f"/tmp/{today}_dice_admin_storage_report.csv")

    headers, report = generate_storage_report(paths, resolve_usernames)
    if not print_to_console:
        write_list_data_to_csv(report, headers, cast(Path, output_file))
        admin_logger.info(f"Report saved to {output_file}")
    else:
        admin_logger.info(tabulate(report, headers=headers, tablefmt="psql"))

    headers, report = generate_storage_report(paths, resolve_usernames)
    write_list_data_to_csv(report, headers, cast(Path, output_file))


@app.command()
def consistency_check_grid(
    grid_endpoint: str = typer.Argument(...),
    storage_endpoint: str = typer.Argument(...),
    output_file: Optional[Path] = typer.Option(
        None,
        "-o",
        "--output",
        help="Output file",
    ),
) -> None:
    """
    Generate a consistency check report for a grid endpoint and the underlying storage.

    :param grid_endpoint: The grid endpoint to generate the report for.
    :param storage_endpoint: The storage endpoint to generate the report for.
    :param output_file: The file to write the report to.
    """
    admin_logger.warning(":construction: Work in progress :construction:")


@app.command()
def network(
    ip_network: str = typer.Argument(...),
    output_file: Optional[Path] = typer.Option(
        None,
        "-o",
        "--output",
        help="Output file",
    ),
    print_to_console: bool = typer.Option(
        False, "--print", help="Print to console instead of output file"
    ),
) -> None:
    """
    Generate a report of the devices connected to the specified network.

    :param ip_network: The network to generate the report for, e.g. 10.129.5.0/24
    :param output_directory: The directory to write the report to.
    """
    if not output_file and not print_to_console:
        today = current_formatted_date()
        output_file = Path(f"/tmp/{today}_dice_admin_network_report.csv")

    admin_logger.warning(":construction: Work in progress :construction:")
    from ._network import _scan_network

    all_hosts = _scan_network(ip_network)
    admin_logger.info(f"Found {len(all_hosts)} hosts")
