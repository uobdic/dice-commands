from ..logger import admin_logger
from ..io import write_list_data_as_dict_to_csv
from ..utils import current_fqdn


def _read_groups() -> list:
    with open("/etc/group") as f:
        group_lines = f.readlines()
    groups = []
    for line in group_lines:
        line = line.split(":")
        groups.append({"name": line[0], "gid": line[2]})
    return groups


def _read_users() -> list:
    with open("/etc/passwd") as f:
        user_lines = f.readlines()
    users = []
    for line in user_lines:
        line = line.split(":")
        users.append({"name": line[0], "uid": line[2], "gid": line[3]})
    return users


def _write_users_to_csv(users: list, output_file: str = "/tmp/users.csv"):
    write_list_data_as_dict_to_csv(users, output_file, ["name", "uid", "gid"])


def _write_groups_to_csv(groups, output_file="/tmp/groups.csv"):
    write_list_data_as_dict_to_csv(groups, output_file, ["name", "gid"])


def main():
    groups = _read_groups()
    users = _read_users()
    hostname = current_fqdn()

    user_output = f"/tmp/00_{hostname}_users.csv"
    group_output = f"/tmp/01_{hostname}_groups.csv"

    _write_users_to_csv(users, user_output)
    _write_groups_to_csv(groups, group_output)

    admin_logger.info(f"Wrote users to {user_output}")
    admin_logger.info(f"Wrote groups to {group_output}")
