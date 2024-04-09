#!/usr/bin/python3
"""Fabric script to deploy an archive to web servers"""

from fabric.api import *
from os.path import exists

env.hosts = ['52.91.184.90', '35.174.211.198']
env.user = 'ubuntu'  # Update with your username
env.key_filename = ['root/.ssh/id_rsa']  # Update with your SSH private key path

def do_deploy(archive_path):
    """Distributes an archive to web servers"""

    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')
        print("put")

        # Extract the archive to /data/web_static/releases/<archive filename without extension>
        filename = archive_path.split('/')[-1]
        folder_name = '/data/web_static/releases/{}'.format(filename.split('.')[0])
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(filename, folder_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))

        # Move the contents of the extracted folder to the proper location
        run('mv {}/web_static/* {}'.format(folder_name, folder_name))

        # Remove the extracted folder
        run('rm -rf {}/web_static'.format(folder_name))

        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the deployed folder
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True
    except:
        return False
