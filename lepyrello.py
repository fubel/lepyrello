#!/usr/bin/env python

''' Script that updates ID3 track number (TRCK) from a dictionary of audio files 
	from information stored in the movement tag (TPOS).
	Numbers the files in correct order.

	Meant for converting mp3 files used on mp3-players which don't use the TPOS
	and prevent the mess that would happen otherwise.

	TODO:
			*	Optimize code: This is the first commit. Code could be faster.
			*	Deal with Exceptions: If some files in the directory are no 
									  music files or have no ID3 frame...
			*	Build a GUI: To make this useful to a normal user
			*	Generalize the code to sort by other ID3 tags in similar way 
			*	Modulize this 
'''

# System imports
import os
import pathlib
import operator

from collections import OrderedDict

# Third party imports
from mutagen.id3 import ID3, TPOS, TRCK

def get_audio_tpos(audio):
	return str(audio.get('TPOS')).split('/')[0]

def get_audio_track(audio):
	return str(audio.get('TRCK')).split('/')[0]

def set_id3_track(audio, nr):
	nr = str(nr)
	nr = nr + "/" + nr
	audio.add(TRCK(encoding=1, text=nr))
	audio.save()

def generate_movement_dict(audios):
	mvmts = OrderedDict()
	files_in_dir = [str(p) for p in pathlib.Path(audios).iterdir() if p.is_file()]
	for audio in files_in_dir:
		audio_tpos = get_audio_tpos(ID3(audio))
		audio_track = int(get_audio_track(ID3(audio)))
		try:
			mvmts[audio_tpos].append((audio, audio_track))
		except KeyError:
			mvmts[audio_tpos] = [(audio, audio_track)]
	for k in mvmts:
		mvmts[k].sort(key=operator.itemgetter(1))

	return mvmts

def number_audios(dictionary):
	j = 1
	keylist = []
	for key in dictionary:
		for audio in dictionary[key]:
			audio = audio[0]
			path, filename = os.path.split(audio)
			audio_new = os.path.join(path, str(j) + ' ' + filename)
			os.rename(audio, audio_new)
			set_id3_track(ID3(audio_new), j)
			j = j+1
	return j

def update_id3_max_track(audios, max_track):
	files_in_dir = [str(p) for p in pathlib.Path(audios).iterdir() if p.is_file()]
	for audio in files_in_dir:
		audio = ID3(audio)
		set_id3_track(audio, max_track)

def movements_to_track(directory):
	movements = generate_movement_dict(directory)
	print(movements)
	max_track = number_audios(movements)
	# update_id3_max_track(directory, max_track)
	print("finished.")


if __name__ == "__main__":
    movements_to_track("/home/fabianfubel/nfblm/")