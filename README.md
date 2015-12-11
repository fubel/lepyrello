# lepyrello

lepyrello is a Python script that converts audio files with ID3-movement-tag (TPOS) into audio files using ID3-track-number-tag (TRCK) only. It also numbers the audio filenames in correct order. I did this because my mp3-player does not know the TPOS-tag and therefore messes up  classical music album trackings on a regular basis.

## Installation

You need Python 3.4+ to execute the script.

	git clone git@github.com:fubel/lepyrello.git
	pip install mutagen

## Usage

	python lepyrello.py -d /your/music/directory/

## Example

Let a record of 'Don Giovanni' be located in /home/music/giovanni/ with the following files:

| FILENAME                     | ID3-TRACK | ID3-TPOS |
|------------------------------|-----------|----------|
| Overture.mp3                 | 1         | 1        |
| Notte e giorno faticar.mp3   | 2         | 1        |
| Leporello, ove sei.mp3       | 3         | 1        |
| Ma qual mai s'offre.mp3      | 4         | 1        |
| ...                          | ...       | ...      |
| Eh via, buffone.mp3          | 1         | 2        |
| ...                          | ...       | ...      |
| Ah! pieta, signorie miei.mp3 | 13        | 2        |

The command

    python lepyrello.py -d /your/music/directory/

will convert this to

| FILENAME                        | ID3-TRACK | ID3-TPOS |
|---------------------------------|-----------|----------|
| 01-Overture.mp3                 | 1         | 1        |
| 02-Notte e giorno faticar.mp3   | 2         | 1        |
| 03-Leporello, ove sei.mp3       | 3         | 1        |
| 04-Ma qual mai s'offre.mp3      | 4         | 1        |
| ...                             | ...       | ...      |
| 19-Eh via, buffone.mp3          | 19        | 1        |
| ...                             | ...       | ...      |
| 32-Ah! pieta, signorie miei.mp3 | 32        | 1        |

so the first track of TPOS 2 is now the next track of the last track of TPOS 1 and so on...