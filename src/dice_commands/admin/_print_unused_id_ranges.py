from itertools import count, groupby

from ..logger import admin_logger
from ..io import read_ints_from_csv
from ..utils import as_range


def _read_userids(filename):
    return read_ints_from_csv(filename, 'uid')


def _read_groupids(filename):
    return read_ints_from_csv(filename, 'gid')


def main(users_file: str, group_file: str) -> None:
    """
    Prints the unused ID ranges for all groups and users.
    """
    userids = _read_userids(users_file)
    groupids = _read_groupids(group_file)

    unused_uids = sorted(set([i for i in range(max(userids))]) - set(userids))
    unused_uids_ranges = ",".join(
        as_range(g) for _, g in groupby(unused_uids, key=lambda n, c=count(): n - next(c))
    )

    unused_gids = sorted(set([i for i in range(max(groupids))]) - set(groupids))
    unused_gids_ranges = ",".join(
        as_range(g) for _, g in groupby(unused_gids, key=lambda n, c=count(): n - next(c))
    )

    admin_logger.debug(f"Used UIDs: {userids}")
    admin_logger.info(f"Unused UID ranges: {unused_uids_ranges}")

    admin_logger.debug(f"Used GIDs: {groupids}")
    admin_logger.info(f"Unused GID ranges: {unused_gids_ranges}")