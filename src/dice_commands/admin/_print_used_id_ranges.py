import csv
from itertools import count, groupby
import os
import sys

from ..logger import admin_logger

def _as_range(iterable):
    """From https://codereview.stackexchange.com/q/5196"""
    l = list(iterable)
    if len(l) > 1:
        return "{0}-{1}".format(l[0], l[-1])
    else:
        return "{0}".format(l[0])


def main(users_file: str, group_file: str) -> None:
    """
    Prints the used ID ranges for all groups and users.
    """
    with open(users_file, 'r') as f:
        reader = csv.DictReader(f, delimiter=",", quotechar='"')
        userids = [int(row['uid']) for row in reader]
        userids.sort()

    with open(group_file, 'r') as f:
        reader = csv.DictReader(f, delimiter=",", quotechar='"')
        groupids = [int(row['gid']) for row in reader]
        groupids.sort()

    uid_ranges = ",".join(_as_range(g) for _, g in groupby(userids, lambda x, c=count(): next(c) - x))
    gid_ranges = ",".join(_as_range(g) for _, g in groupby(groupids, lambda x, c=count(): next(c) - x))

    admin_logger.info("Used UID ranges: {0}".format(uid_ranges))
    admin_logger.info("Used GID ranges: {0}".format(gid_ranges))
