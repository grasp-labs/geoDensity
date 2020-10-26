# src/config/db/config.py
from config.settings import CONFIG


def config(section=None):
    """
    Database configuration for application
    """
    parser = CONFIG
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the file'.format(section))
    return db
