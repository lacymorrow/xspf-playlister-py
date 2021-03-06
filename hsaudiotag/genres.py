# Created By: Virgil Dupras
# Created On: 2007/05/12
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)

# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

MUSIC_GENRES = (
u"Blues",
u"Classic Rock",
u"Country",
u"Dance",
u"Disco",
u"Funk",
u"Grunge",
u"Hip-Hop",
u"Jazz",
u"Metal",
u"New Age",
u"Oldies",
u"Other",
u"Pop",
u"R&B",
u"Rap",
u"Reggae",
u"Rock",
u"Techno",
u"Industrial",
u"Alternative",
u"Ska",
u"Death Metal",
u"Pranks",
u"Soundtrack",
u"Euro-Techno",
u"Ambient",
u"Trip-Hop",
u"Vocal",
u"Jazz+Funk",
u"Fusion",
u"Trance",
u"Classical",
u"Instrumental",
u"Acid",
u"House",
u"Game",
u"Sound Clip",
u"Gospel",
u"Noise",
u"AlternRock",
u"Bass",
u"Soul",
u"Punk",
u"Space",
u"Meditative",
u"Instrumental Pop",
u"Instrumental Rock",
u"Ethnic",
u"Gothic",
u"Darkwave",
u"Techno-Industrial",
u"Electronic",
u"Pop-Folk",
u"Eurodance",
u"Dream",
u"Southern Rock",
u"Comedy",
u"Cult",
u"Gangsta",
u"Top 40",
u"Christian Rap",
u"Pop/Funk",
u"Jungle",
u"Native American",
u"Cabaret",
u"New Wave",
u"Psychadelic",
u"Rave",
u"Showtunes",
u"Trailer",
u"Lo-Fi",
u"Tribal",
u"Acid Punk",
u"Acid Jazz",
u"Polka",
u"Retro",
u"Musical",
u"Rock & Roll",
u"Hard Rock",

u"Folk",
u"Folk-Rock",
u"National Folk",
u"Swing",
u"Fast Fusion",
u"Bebob",
u"Latin",
u"Revival",
u"Celtic",
u"Bluegrass",
u"Avantgarde",
u"Gothic Rock",
u"Progressive Rock",
u"Psychedelic Rock",
u"Symphonic Rock",
u"Slow Rock",
u"Big Band",
u"Chorus",
u"Easy Listening",
u"Acoustic",
u"Humour",
u"Speech",
u"Chanson",
u"Opera",
u"Chamber Music",
u"Sonata",
u"Symphony",
u"Booty Bass",
u"Primus",
u"Porn Groove",
u"Satire",
u"Slow Jam",
u"Club",
u"Tango",
u"Samba",
u"Folklore",
u"Ballad",
u"Power Ballad",
u"Rhythmic Soul",
u"Freestyle",
u"Duet",
u"Punk Rock",
u"Drum Solo",
u"A capella",
u"Euro-House",
u"Dance Hall",
u"Goa",
u"Drum & Bass",
u"Club-House",
u"Hardcore",
u"Terror",
u"Indie",
u"BritPop",
u"Negerpunk",
u"Polsk Punk",
u"Beat",
u"Christian",
u"Heavy Metal",
u"Black Metal",
u"Crossover",
u"Contemporary",
u"Christian Rock",
u"Merengue",
u"Salsa",
u"Thrash Metal",
u"Anime",
u"JPop",
u"Synthpop")

def genre_by_index(index):
    return MUSIC_GENRES[index] if index >= 0 and index < len(MUSIC_GENRES) else u''

