#!/usr/bin/env python -O
import os, sys, re, fnmatch, ntpath
from hsaudiotag import auto
#import sys
#import re
#import fnmatch
#import ntpath

# playlister.py
# Mark Talbert & Lacy Morrow
# Given a root directory, this script will build an XSPF playlist

def scanMedia(path):
	#"main" routine
	confirmExistence(path)
	formatPath(path)
	playArr = []
	imgArr = []
	types = ['*.mp3']#,'*.wav','*.ogg','*.mp4','*.webm','*.ogv','*.jpg','*.jpeg','*.gif','*.png']
	types = r'|'.join([fnmatch.translate(x) for x in types])

	#mp3s = [os.path.join(root, i) for root, dirs, files in os.walk(path) for i in files if i[-3:] == "mp3"] #preliminary functionality
	media = [os.path.join(root, x) for root, dirs, files in os.walk(path) for x in files if re.match(types, x)]
	
	for file in media:
		#print file
		file = os.path.abspath(file).rstrip('\0')
		name, ext = os.path.splitext(file)
		type = checkType(ext).rstrip('\0')
		
		if type == 'image':
			info = { 'image': file,
					 'filename' : fileNameOnly(file) }
			#print fileNameOnly(file)			
			imgArr.append(info)
		elif type == 'audio':
			meta = auto.File(file)#getID3v1(file)
			title = meta.title.rstrip('\0')
			artist = meta.artist.rstrip('\0')
			album = meta.album.rstrip('\0')
			comment = meta.comment.rstrip('\0')
			duration = meta.duration
			location = []
			location.append(file)
			info = 		{ 'filename' : title,
						'type' : type, 
						'creator' : artist, 
						'album' : album,
						'title' : title, 
						'comment' : comment,
						'duration' : duration, 
						'location' : location, 
						'image' : '', 
						'info' : type,
						#'path' : file 
										}
			#print title		  
			playArr.append(info)

		#playArr[title] = OrderedDict([('filename',title),
		#			                   ('type',checkType(ext).rstrip('\0')),
        #  				               ('creator',artist),
        #                              ('album',album),
        #                              ('title',title),
		#						       ('annotation',annotation),
        #                              ('path',track)])
		
		#		} else {
	    #	// Apply album/creator image
		#			for ($k=0;$k<sizeOf($gloArr);$k++){
		#				if ($gloArr[$k]['path'] == $playVal['path']){
		#					$playVal['image'] = ''.$gloArr[$k]['path'].'/'.$gloArr[$k]['file'];
		#				}
		#			}
		#		}
		#	}
		
		for playVal in playArr:
			for i in range(0,len(imgArr)):
				if imgArr[i]['filename'] == playVal['filename']:
					playVal['image'] = imgArr[i]['image']
    	#//echo $globalImg;
    	#// Apply global image
		#	if($playVal['image'] == '' && $globalImg != ''){ $playVal['image'] = $globalImg; }
    	
	return playArr

def generateXML(playArr):
	from cgi import escape
	out = '<?xml version="1.0" encoding="UTF-8"?>' + '\n'
	out += '<playlist version="1" xmlns="http://xspf.org/ns/0/">' + '\n'
	out += '  <trackList>' + '\n'
	for l in playArr:
		out += '    <track>' + '\n'
		for i in l['location']:
			out += '      <location>' + escape(i).encode('ascii', 'xmlcharrefreplace') + '</location>' + '\n'
		out += '      <creator>' + l['creator'] + '</creator>' + '\n'
		out += '      <album>' + l['album'] + '</album>' + '\n'
		out += '      <title>' + l['title'] + '</title>' + '\n'
		out += '      <annotation>' + l['comment'] + '</annotation>' + '\n'
		out += '      <duration>' + str(l['duration']) + '</duration>' + '\n'
		out += '      <image>' + l['image'] + '</image>' + '\n'
		#out += '      <info>' + l['info'] + '</info>' + '\n'
		out += '      <type>' + l['info'] + '</type>' + '\n'
		out += '    </track>' + '\n'
	out += '  </trackList>' + '\n'
	out += '</playlist>'
	return out
	
def getID3v1(file):

	fp = open(file, 'r')
	fp.seek(-128, 2)
	fp.read(3)
	title = fp.read(30)
	artist = fp.read(30)
	album = fp.read(30)
	annotation  = fp.read(4)
	comment = fp.read(28)
	fp.close()
	return {
		'title':title,
		'artist':artist,
		'album':album,
		'annotation':annotation,
		'comment':comment }

def checkType(ext):

	musTypes = ( '.mp3','.wav','.ogg' )
	vidTypes = ( '.mp4','.webm','.ogv' )
	picTypes = ( '.jpg', '.jpeg', '.gif', '.png' )

	if ext in musTypes:
		return 'audio'
	elif ext in picTypes:
		return 'image'
	elif ext in vidTypes:
		return 'video'
	else:
		return 'invalid'

def fileNameOnly(path):
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)

def toString(dict):
	return ', '.join("%s = %r" % (key,val) for (key,val) in dict.iteritems())
	
def relPath(absPath):
	pass
	
def formatPath(path):
    #format path to be os-specific
    return path.replace('/',os.sep)	
	
def confirmExistence(path):
	#implement error logging so exceptions like these will end up somewhere useful upon error
	if not os.path.isdir(path):
		raise OSError, 'Path %s is not a directory' % path
		sys.exit(1)
	if not os.path.exists(path):
		raise OSError, 'Path %s does not exist' % path
		sys.exit(1)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'usage: python playlister.py [absolute path]'
		sys.exit(1)
	#Windows filepath may contain spaces. Merge into single string.
	if len(sys.argv) > 2:
		path = ' '.join([x for x in sys.argv[1::1]])
		xml = generateXML(scanMedia(path))
		print xml
	else:
		xml = generateXML(scanMedia(sys.argv[1]))
		print xml
		