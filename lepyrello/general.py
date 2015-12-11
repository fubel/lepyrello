"""
Collection of functions that have nothing to do with id3-tags
but are needed for different lepyrello functions.
"""

# Python imports
import pathlib
from collections import OrderedDict

# Lepyrello imports
from id3 import audio
from exceptions import NotAnAudioFileException, TagNotSupportedException


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


def generate_audio_dict(tag, audio_list):
    """
    Takes an id3-tag (e.g. TPOS) and an audio_list and
    produces a sorted dictionary. For example, if the tag is TPOS, it will
    create:

        (1: [list of audios with TPOS 1 in correct track order],
         2: [list of audios with TPOS 2 movement in correct track order], ...)
    """
    supported_tags = ["TPOS"]
    if not tag in supported_tags:
        raise TagNotSupportedException(tag)

    pass
