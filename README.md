xspf-playlister 0.0.1
==================

Generate an XSPF playlist file for audio and video files using Python. 

Use it on the command line once or as a dead-simple way to keep a playlist on the internet up to date. 

## Usage
Place all of your media files into a folder called `media`. Copy `playlister.py` and the `hsaudiotag` directory to the same location as the media directory. Run `playlister.py` to generate and print your XSPF file. That's it!

Supports `mp3`, `wav`, and `ogg` audio and `mp4`, `webm`, and `ogv` video formats. If two files of different types share a filename, they will be interpreted as two sources for the same track. Tracks will be titled by their filename sans extension. Additional creator and album information can be provided by organizing your files into a media/creator/album/file hierarchy. An image may be associated with a track by giving it the same filename. To associate one image with an entire folder of tracks, give it the filename `artwork`. `artwork` images associate themselves to every sibling and child directory and may be placed anywhere in your media directory hierarchy, so an `artwork.jpg` in the `media` directory will act as a global image, filling in for every track that did not already have one provided.

By default, the [hsaudiotag](https://github.com/hsoft/hsaudiotag/) library is used to scan `mp3` files and will automatically use the meta information associated with a track, rather than the menu directory hierarchy.


## Usage:
`python playlister.py /absolute/path/to/media/ > playlist.xspf`