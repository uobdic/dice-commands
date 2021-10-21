import logging

from .utils import current_linux_user, current_date

admin_logger = logging.getLogger("dice_admin")
admin_logger.setLevel(logging.INFO)

user_logger = logging.getLogger("dice_user")
user_logger.setLevel(logging.INFO)

console_formatter = logging.Formatter("%(asctime)s [%(name)s]  %(levelname)s: %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)

logfile_handler = logging.FileHandler(f"/tmp/dice_commands_{current_linux_user()}_{current_date()}.log")
logfile_handler.setLevel(logging.DEBUG)

admin_logger.addHandler(console_handler)
admin_logger.addHandler(logfile_handler)

user_logger.addHandler(console_handler)
user_logger.addHandler(logfile_handler)

