import codecs
from random import shuffle


class Song:
    def __init__(self, artist, name, album, position, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.position = position
        self.year = year
        self.duration = duration  
        
    def __repr__(self):
        song = "\"%s\" \t %s \t %s \t %s \t %s \t %s" % (self.name, self.artist, self.album, self.position, self.year, self.duration)
        return song
        
        
def import_songs(file_name):
    inf = codecs.open(file_name, "r", "utf_8_sig")
    songs = inf.readlines()
    inf.close()
    songs_list = []
    for line in songs:
        artist, name, album, position, year, duration = line.split("\t")[0:6]
        songs_list.append(Song(name, artist, album, position, year, duration))
    return songs_list


def export_songs(songs, file_names):
    with open(file_names, "w") as of:
        for line in songs:
            of.write(str(line))


def shuffle_songs(songs):
    shuffle(songs) 
    return songs
    
song_list = import_songs("songs1.txt")


def most_freq(song_list):
    artists = []
    most_freq_artist = []
    artist_count = {}
    for song in song_list:
        artists.append(song.artist)
    artists.sort()    
    for artist in artists:
        if artist in artist_count:
            artist_count[artist] += 1
        else:
            artist_count[artist] = 1
    for key, value in artist_count.items():
        if value == max(artist_count.values()):
            most_freq_artist.append(key)
    shuffle(most_freq_artist) 
    return most_freq_artist[0]


def most_lengthy(song_list):
    songs_lent = []
    most_lengthy_song = []
    for song in song_list:
        songs_lent.append((song.name + "\t" + song.artist, int(song.duration)))

    songs_lent = dict(songs_lent)

    for key, value in songs_lent.items():
        if value == max(songs_lent.values()):
            most_lengthy_song.append(key)
    shuffle(most_lengthy_song)         
    return most_lengthy_song[0]
    
    
def most_lengthy_album(song_list_in):
    album_duration = 0
    albums = {}
    most_lengthy_album = []
    song_list_in.append(Song("X", "X", "X", "X", "X", 0))
    for i in range(len(song_list_in) - 1):
        if song_list_in[i].artist + "\t" + song_list_in[i].album == song_list_in[i + 1].artist + "\t" + song_list_in[i + 1].album:
            album_duration += int(song_list_in[i].duration)
        else:
            albums[song_list_in[i].album + "\t" + song_list_in[i].artist] = album_duration + int(song_list_in[i].duration)
            album_duration = 0
    for key, value in albums.items():
        if value == max(albums.values()):
            most_lengthy_album.append(key)
    shuffle(most_lengthy_album)
    song_list_in.remove(song_list_in[len(song_list_in) - 1])
    return most_lengthy_album[0]


def freq_words(song_list):
    words = ""
    symbols = ["q", 'w', "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
                    "x", "v", "b", "n", "m", " "]
    freq_words = {}
    dictlist = []
    dictout = ""
    for song in song_list:
        words += song.name.lower().replace("'", " ").replace("-", " ").replace(".", " ").replace("  ", " ") + " "
    words = (''.join([c for c in list(words) if c in symbols])).split()
    for word in words:
        if word in freq_words:
            freq_words[word] += 1
        else:
            freq_words[word] = 1
    for key, value in freq_words.items():
        temp = [value, key]
        dictlist.append(temp)
    dictlist.sort(reverse=True)
    if len(dictlist) >= 10:
        for i in dictlist[:10]:
            dictout += i[1] + "\t"
    else:
        for i in dictlist:
            dictout += i[1] + "\t"
    return dictout


def most_freq_album(song_list):
    artist_album = []
    artists = []
    most_freq_artist = []
    artist_count = {}
    for song in song_list:
        if song.artist + "\t" + song.album not in artist_album:
            artist_album.append(song.artist + "\t" + song.album)
            artists.append(song.artist)    
    for artist in artists:
        if artist in artist_count:
            artist_count[artist] += 1
        else:
            artist_count[artist] = 1
    for key, value in artist_count.items():
        if value == max(artist_count.values()):
            most_freq_artist.append(key)
    shuffle(most_freq_artist) 
    return most_freq_artist[0]


print(most_freq(song_list))
print(most_lengthy(song_list))
print(most_lengthy_album(song_list))
print(freq_words(song_list))
print(most_freq_album(song_list))