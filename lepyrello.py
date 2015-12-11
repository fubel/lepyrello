#!/usr/bin/env python
import argparse 

from lepyrello.general import get_audio_list, generate_audio_dict
from lepyrello.converters import tpos_to_trck

def main():
    parser = argparse.ArgumentParser(description='lepyrello id3 tag converter')
    parser.add_argument('-d', dest='directory', help='directory containing the music')
    parser.add_argument('-ttt', dest='ttt', help='use tpos to track converter', action="store_true")
    args = parser.parse_args()

    if not args.directory:
        parser.print_help()
        parser.exit(1)

    if args.ttt:
        print("Started TPOS-to-TRACK converter for %s" % args.directory)
        audio_list = get_audio_list(args.directory)
        audio_dict = generate_audio_dict("TPOS", audio_list)
        tpos_to_trck(audio_dict)
        print("Done.")


if __name__ == "__main__":
    main()
