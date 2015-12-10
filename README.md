# lepyrello

lepyrello is a Python script that converts audio files with ID3-movement-tag (TPOS) into audio files using ID3-track-number-tag (TRCK) only. It also numbers the audio filenames in correct order. I did this because my mp3-player does not know the TPOS-tag and therefore messes classical music albums on a regular basis.

## Installation

You need Python 3.4+ to execute the script.

	git clone git@github.com:fubel/lepyrello.git
	pip install mutagen

## Usage

	python lepyrello.py -d /your/music/directory/
