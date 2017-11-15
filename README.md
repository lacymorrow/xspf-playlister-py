xspf-playlister 0.1.0
==================

> *It actually works pretty well!*

Generate an XSPF playlist file for audio and video files using PHP.

_A PHP implementation of the XSPF Playlist Generator ported here: https://github.com/lacymorrow/xspf-playlister-php_

Created for: [lacymorrow/xspf-jukebox](https://github.com/lacymorrow/xspf-jukebox).


## File Types

Supports `mp3`, `wav`, and `ogg` audio and `mp4`, `webm`, and `ogv` video formats. 

If two video files of different types share a filename, they will be interpreted as two sources for the same track. 

Tracks will be titled by their filename sans extension. Additional creator and album information can be provided by organizing your files into a media/creator/album/file hierarchy. 

An image may be associated with a track by giving it the same filename. To associate one image with an entire folder of tracks, give it the filename `artwork`. `artwork` images associate themselves to every sibling and child directory and may be placed anywhere in your media directory hierarchy, so an `artwork.jpg` in the `media` directory will act as a global image, filling in for every track that did not already have one provided.

By default, the [getid3](http://getid3.sourceforge.net/) library is used to scan `mp3` files and will automatically use the meta information associated with a track, rather than the menu directory hierarchy. In order to alleviate server load, a small caching mechanism is in place. 

By default the playlist is cached every hour. Open `playlister.py` and edit the settings to change the functionality or provide a different media directory.

#### Command Line:

`php playlister.php path/to/media > playlist.xspf`


## License

[MIT](http://opensource.org/licenses/MIT) © [Lacy Morrow](http://lacymorrow.com)

## 
Generate an XSPF playlist file for audio and video files using Python 2. 

Use it on the command line once or as a dead-simple way to keep a playlist on the internet up to date. 

## Usage
Place all of your media files into a folder called `media`. Copy `playlister.py` and the `hsaudiotag` directory to the same location as the media directory. Run `playlister.py` to generate and print your XSPF file. That's it!

Supports `mp3`, `wav`, and `ogg` audio and `mp4`, `webm`, and `ogv` video formats. If two files of different types share a filename, they will be interpreted as two sources for the same track. Tracks will be titled by their filename sans extension. Additional creator and album information can be provided by organizing your files into a media/creator/album/file hierarchy. An image may be associated with a track by giving it the same filename. To associate one image with an entire folder of tracks, give it the filename `artwork`. `artwork` images associate themselves to every sibling and child directory and may be placed anywhere in your media directory hierarchy, so an `artwork.jpg` in the `media` directory will act as a global image, filling in for every track that did not already have one provided.

By default, the [hsaudiotag](https://github.com/hsoft/hsaudiotag/) library is used to scan `mp3` files and will automatically use the meta information associated with a track, rather than the menu directory hierarchy.


## Usage:
`python playlister.py /absolute/path/to/media/ > playlist.xspf`


## License

[MIT](http://opensource.org/licenses/MIT) © [Lacy Morrow](http://lacymorrow.com)
