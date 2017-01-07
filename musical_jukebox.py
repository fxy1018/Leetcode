"""
Design a musical jukebox using object-oriented design

Basic System Components:
    Jukebox
    CD
    Song
    Artist
    Playlist
    Display (displays details on the screen)

Possible Actions:
    Playlist creation (add, delete, and shuffle)
    CD selector
    Song selector
    Queuing up a song
    Get next song from playlist

A user also can be introduced:
    Adding 
    Deleting
    Credit information

"""

'''
Created on Jan 6, 2017

@author: fanxueyi
'''
from collections import deque

class Jukebox(object):
    def __init__(self, cdPlayer, user, cds, ts):
        self.CDPlayer = cdPlayer
        self.user = user
        self.CD = set(cds)
        self.SongSelector = ts
    
    def getCurrentSong(self):
        return(self.SongSelector.getCurrentSong)
    
    def setUser(self,name,iD):
        self.user = User(name,iD)
        
class SongSelector(object):
    def __init__(self, CD, PlayList):
        self.cd = CD
        self.playlist = PlayList
    
    def getNextSong(self):
        return
    
    def removeSong(self):
        return
    

class CDPlayer(object):
    def __init__(self, CD, playlist):
        self.playlist = playlist
        self.CD = CD
        
    def playSong(self):
        return
    
    def getPlayList(self):
        return(self.playlist)
    
    def setPlayList(self, songs):
        self.playlist = PlayList(songs)
    
    def getCD(self):
        return(self.CD)
    
    def setCD(self, iD):
        self.CD = CD(iD)
        
        


class PlayList(object):
    def __init__(self,songs):
        songs = deque(songs)
        self.song = songs
        
    
    def getNextSong(self):
        return(self.songs[1])
    
    def queueUpSong(self, newsong):
        self.song.append(newsong)
          

class CD(object):
    def __init__(self):
        #data for id, CD (could be null), title, length, etc
        self.id = ""

class Song(object):
    def __init__(self):
        #data for id, artist, songs, etc 
        self.id = ""
        
        
class User(object):
    def __init__(self, name, iD):
        self.name = name
        self.ID = iD
    
    def getName(self):
        return(self.name)
    
    def setName(self, newname):
        self.name = newname
    
    def setID(self, iD):
        self.ID = id
        
    def getID(self):
        return(self.ID)
    
    def getUser(self):
        return(self)

    def addUser(self, name, iD):
        newUser = User(name,iD)
        return(newUser)



