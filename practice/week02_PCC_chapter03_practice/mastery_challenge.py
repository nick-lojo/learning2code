playlist = []
playlist.append('song_a')
playlist.append('song_b')
playlist.append('song_c')

playlist.remove('song_b')

playlist.insert(0, 'song_d')

print(playlist[-1])

print(len(playlist))

playlist.sort()
print(playlist)