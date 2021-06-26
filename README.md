This will "download" (actually copy) a playlist from plex to a different local folder. Assuming your computer and plex have the same network share mounted, although at different directories. It's written for linux, but you can problably get it to work for windows? See --help for instructions.

# Dev Notes
* You can set the help pager by doing `PAGER=cat ./plex-list-downloader.py`

# Cleanup Filenames
For me, the best way I found to fix the filenames is to run something like picard to make sure the tags are in order, then use soundconverter to make the filenames match the tags.

Next time I touch this I'll try to provide a config and command line to do that.
