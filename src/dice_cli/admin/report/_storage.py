from pathlib import Path
from typing import List

from dice_lib.fs import get_owner, size_of_paths
from dice_lib.user import get_user_full_name

from dice_cli._io import write_list_data_to_csv


def _resolve_usernames_in_report(report):
    new_report = []
    for row in report:
        path = row[0]
        owner = get_owner(path)
        full_name = get_user_full_name(owner)
        new_report.append(row + (owner, full_name))
    return new_report


def generate_storage_report(
    paths: List[Path], output_directory: Path, resolve_usernames: bool
) -> None:
    """
    Generates a storage report for a list of paths.

    :param paths: List of paths to generate a report for.
    :param output_directory: Directory to write the report to.
    :param resolve_usernames: Whether to resolve usernames to full names.
    """
    headers = ["Path", "Size [B]", "Size [human-readable]", "Unit [human-readable]"]
    report = size_of_paths(paths)
    if resolve_usernames:
        headers += ["Owner", "Owner full name"]
        report = _resolve_usernames_in_report(report)

    write_list_data_to_csv(report, headers, output_directory)
