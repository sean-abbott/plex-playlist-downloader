#!/usr/bin/env python

import fire

import os
import re
import shutil
import sys

from plexapi.myplex import MyPlexAccount

def download_playlist(playlist_name, dest_path, username=None, password=None, server=None, plex_dir=None, local_dir=None):
    """Download a plex playlist to the destination_path (dest_path)

    This does require your plex username, password, and server. be sure to clear your command line history for security.

    This will move the files from a playlist into the dest_path.

    This assumes that you're on a personal computer that is mounting the same network share your plex server is, but want to
    download files from a playlist to a local directory. For instance, if you want to download a playlist to a usb drive to
    put on your car's harddrive or give to a partner

    Positional Arguments:
        playlist_name - the name of the playlist. Be sure to double quote from the command line
        dest_path - the top level directory where you want media files stored. i.e. /media/account/usb-drive

    Keyword Arguments:
        plex_dir - the directory that the source file are mounted on your plex server. This will be replaced with your local_dir.
                   For example, /data
        local_dir - The directory that the source files are mounted locally. This will replace your plex dir.
                    For example, /home/username/net/music
    """
    _verify_requirements(username, password, server)

    print(f'Download "{playlist_name}" to "{dest_path}"')

    plex = _get_server(username, password, server)

    playlist = plex.playlist(playlist_name)

    src_list = [_get_source_path(d.locations[0], plex_dir=plex_dir, local_dir=local_dir) for d in playlist.items()]
    print(f'Destination directory {dest_path}')
    for f in src_list:
        print(f'Copying {os.path.basename(f)}')
        shutil.copy(f, dest_path)
    return

def _verify_requirements(username, password, server):
    if (username is None) or (server is None) or (password is None):
        print('Cannot proceed without username, password, and server. See "--help"')
        sys.exit(1)

def _get_server(username, password, server):
    account = MyPlexAccount(username, password)
    print(account)
    return account.resource('sunplex').connect()

def _get_source_path(path, plex_dir=None, local_dir=None):
    if (plex_dir is None) or (local_dir is None):
        print(f'Assuming that the plex directory and your local directory are the same, since plex_dir and/or local_dir are not set')
        return
    return re.sub(rf'^{plex_dir}', local_dir, path)

if __name__ == '__main__':
    fire.Fire(download_playlist)
