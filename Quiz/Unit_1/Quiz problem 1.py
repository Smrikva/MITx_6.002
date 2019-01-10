#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 18:58:34 2018

@author: smrikva
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    
    music = songs.copy()
    playlist = []
    size = 0
    
    if not len(music) or music[0][-1]>max_size:
        return []
    else:
        size += music[0][-1]
        playlist.append(music.pop(0)[0])
        music.sort(key=lambda x:x[-1])
    
    for song in music:
        if size+song[-1] <= max_size:
            size += song[-1]
            playlist.append(song[0])
        else:
            return playlist

    return playlist

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 12.2

print(song_playlist(songs, max_size))