#!/usr/bin/env python
from __future__ import print_function
import csv

passwd_file = "/etc/passwd"
group_file = "/etc/group"
# get hostname from /etc/hostname
hostname = open("/etc/hostname").read().strip()

with open(passwd_file) as f:
    passwd_lines = f.readlines()

with open(group_file) as f:
    group_lines = f.readlines()

# list user name, UID and GID of all users
users = []
for line in passwd_lines:
    line = line.split(":")
    users.append({"name": line[0], "uid": line[2], "gid": line[3]})

try:
    with open('/tmp/00_' + hostname + "_users.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "uid", "gid"])
        writer.writeheader()
        writer.writerows(users)
except IOError as e:
    print(e)

# list group name, GID and users of all groups
groups = []
for line in group_lines:
    line = line.split(":")
    groups.append({"name": line[0], "gid": line[2]})

# store groups in CSV file
try:
    with open('/tmp/01_' + hostname + "_groups.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "gid"])
        writer.writeheader()
        writer.writerows(groups)
except IOError as e:
    print(e)
