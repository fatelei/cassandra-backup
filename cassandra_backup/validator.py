# -*- coding: utf8 -*-
"""
cassandra_backup.validator.

~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validator.
"""

import os


def validate_path(path):
    """Validate the path is exists or not.

    :param str path: Path
    :return: A boolean.
    """
    return os.path.isdir(path)
