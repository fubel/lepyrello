"""
Collection of functions used to read and manipulate 
id3 tags from audiofiles using mutagen.id3.  
"""

# Lepyrello imports
from exceptions import NotAnAudioFileException

# Third party imports
from mutagen.id3 import *


class audio:

    """
    Lepyrello audio class suited for our converters.
    Contains location of file and it's mutagen.id3. 
    """

    def __init__(self, location):
        self.location = location
        try:
            self.id3 = ID3(location)
        except:
            raise NotAnAudioFileException(location)

    def get_track(self):
        track = str(self.id3.get('TRCK')).split('/')[0]
        return track

    def set_track(self, nr, temp=False):
        nr = str(nr) + "/" + str(nr)
        self.id3.add(TRCK(encoding=1, text=nr))

        # save this only if temp=True
        if not temp:
            self.id3.save()

    def get_tpos(self):
        tpos = str(self.id3.get('TPOS')).split('/')[0]
        return tpos
