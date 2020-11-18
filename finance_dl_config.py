"""Example configuration file for finance_dl.

Configuration entries are defined by defining a top-level function with a name
beginning with `CONFIG_`.  The portion after the `CONFIG_` prefix is the name
of the configuration.

Rather than hard code your usernames and passwords into this configuration
file, you may instead wish to write some code to retrieve them from some
external password store.
"""

import os
import keyring
import getpass

# Directory for persistent browser profiles.
profile_dir = os.path.join(os.getenv('HOME'), '.cache', 'finance_dl')
data_dir = './data'


def set_password_if_none(service: str) -> bool:
    if not keyring.get_password(service, "password"):
        keyring.set_password(service, "password", getpass.getpass())
        return True
    return False


def CONFIG_venmo():
    set_password_if_none('venmo')
    return dict(
        module='finance_dl.venmo',
        credentials={
            'username': 'inderpreet99@gmail.com',
            'password': keyring.get_password('venmo', 'password'),
        },
        output_directory=os.path.join(data_dir, 'venmo'),

        # profile_dir is optional but highly recommended to avoid having to
        # enter multi-factor authentication code each time.
        profile_dir=os.path.join(profile_dir, 'venmo'),
    )
