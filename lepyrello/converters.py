"""
Contains all converters for lepyrello
"""

# Python imports
import os

# Lepyrello imports

# Third party imports


def tpos_to_trck(audio_dict):
    """ 
    Takes a dictionary of lepyrello audios and
    and converts a tpos & trck order into a 
    trck only order.

    See doc for further details.
    """
    n = 1
    max_track = 0
    for k in audio_dict:
        max_track += int(audio_dict[list(audio_dict)[k-1]][-1].get_track())
    
    for k in audio_dict:
        print("here")
        for a in audio_dict[k]:
            print(a.location)
            path, filename = os.path.split(a.location)
            zeroed = str(n).zfill(len(str(max_track)))
            prefix = str(zeroed) + '-'
            a_new  = os.path.join(path, prefix + filename)
            os.rename(a.location, a_new)
            a.location = a_new
            a.set_track(n)
            n = n+1
    return n 
