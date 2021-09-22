#!/usr/bin/env python
from __future__ import print_function
import csv
import sys
import os
from itertools import groupby, count

# from https://codereview.stackexchange.com/questions/5196/grouping-consecutive-numbers-into-ranges-in-python-3-2
def as_range(iterable):  # not sure how to do this part elegantly
    l = list(iterable)
    if len(l) > 1:
        return "{0}-{1}".format(l[0], l[-1])
    else:
        return "{0}".format(l[0])


input_files = sys.argv[1:]
users_file = input_files[0]
group_file = input_files[1]

# read users from CSV file
users = []
with open(users_file, "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
    for row in reader:
        users.append(row)

uids = []
for user in users:
    uids.append(int(user["uid"]))
gids = []
with open(group_file, "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
    for row in reader:
        gids.append(int(row["gid"]))

# find unused UIDs between 0 and max(uids)
unused_uids = sorted(set([i for i in range(max(uids))]) - set(uids))
unused_uids_ranges = ",".join(
    as_range(g) for _, g in groupby(unused_uids, key=lambda n, c=count(): n - next(c))
)

# find unused GIDs between 0 and max(gids)
unused_gids = sorted(set([i for i in range(max(gids))]) - set(gids))
unused_gids_ranges = ",".join(
    as_range(g) for _, g in groupby(unused_gids, key=lambda n, c=count(): n - next(c))
)

print("used UIDs", sorted(uids))
print("unused UIDs", unused_uids[:10])
print("unused UID ranges", unused_uids_ranges)

print("used GIDs", sorted(gids))
print("unused GIDs", unused_gids[:10])
print("Unused GIDs ranges", unused_gids_ranges)
