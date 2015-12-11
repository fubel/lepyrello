"""
Contains all exceptions for lepyrello
"""


class NotAnAudioFileException(Exception):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Not and an audio file: %s" % self.name


class TagNotSupportedException(Exception):

    def __init__(self, tag):
        self.tag = tag

    def __str__(self):
        return "The tag %s is not supported." % self.tag
