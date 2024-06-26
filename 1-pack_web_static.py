#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from web_static folder"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from web_static folder"""

    # Create the 'versions' folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the name of the archive file with the current timestamp
    now = datetime.now()
    archive_name = 'web_static_' + now.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    # Compress web_static folder into the archive
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    # Check if the compression was successful
    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)
        print(result)

if __name__ == "__main__":
    do_pack()
