"""
Collection of functions that have nothing to do with id3-tags
but are needed for different lepyrello functions.
"""

# Python imports
import operator
import pathlib
from collections import OrderedDict

# Lepyrello imports
from lepyrello.id3 import audio
from lepyrello.exceptions import NotAnAudioFileException, TagNotSupportedException


def get_audio_list(location):
    """
    Returns a list of lepyrello.audio items from files 
    in location. Ignores non-audio files. 
    """
    audio_list = []
    for p in pathlib.Path(location).iterdir():
        if p.is_file():
            try:
                audio_list.append(audio(str(p)))
            except NotAnAudioFileException:
                pass

    return audio_list


def generate_audio_dict(tag, audio_list, return_sorted=True):
    """
    Takes an id3-tag (e.g. TPOS) and an audio_list and
    produces a sorted dictionary. For example, if the tag is TPOS, it will
    create:

        (1: [list of audios with TPOS 1 in correct track order*],
         2: [list of audios with TPOS 2 in correct track order*], ...)

    * if return_sorted=True
    """
    supported_tags = ["TPOS"]
    if not tag in supported_tags:
        raise TagNotSupportedException(tag)

    # create unsorted dict
    audio_dict = {}
    for a in audio_list:
        try:
            audio_dict[int(a.get_tpos())].append(a)
        except KeyError:
            audio_dict[int(a.get_tpos())] = [a]

    # sort items by their track
    for t in audio_dict:
        audio_dict[t].sort(key=operator.attrgetter("track"))

    # return sorted ordered dict
    return OrderedDict(sorted(audio_dict.items()))

    pass
