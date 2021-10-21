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
    Prints the used ID ranges for all groups and users.
    """
    userids = _read_userids(users_file)
    groupids = _read_groupids(group_file)

    uid_ranges = ",".join(as_range(g) for _, g in groupby(userids, lambda x, c=count(): next(c) - x))
    gid_ranges = ",".join(as_range(g) for _, g in groupby(groupids, lambda x, c=count(): next(c) - x))

    admin_logger.info("Used UID ranges: {0}".format(uid_ranges))
    admin_logger.info("Used GID ranges: {0}".format(gid_ranges))
