# importing other files

from pathlib import Path
import Quotes as qt
import Images as im
import os
import sys
import shutil


def main():

    # The main path is the place where the quote file is kept, along with the videos, and their subtitles
    fortune_file_path = Path(sys.argv[2].replace('\"', ''))
    base_path = Path(sys.argv[1].replace('\"', ''))
    # Modifing the quotes file from the actual fortune format to something managable, with warped lines
    # and removing the quotes that are too big to fit on a photo.
    # base_path = Path(
    #     '/run/media/krishnaraj/Miscellaneous/Programs/Python/Quotepaper Designer/Shows/The Mentalist/s01')

    # fortune_file_path = Path(
    #     '/run/media/krishnaraj/Miscellaneous/Programs/Python/Quotepaper Designer/Shows/The Mentalist/s01/The_Mentalist_(season_1)')
    try:
        os.mkdir(os.path.join(base_path, 'Wallpapers'))
    except:
        print('folders already exist')

    try:
        os.mkdir(os.path.join(base_path, 'Frames'))
    except:
        print('folders already exist')
    qt.modify_quotes(base_path, fortune_file_path)
    # basepath = Path('./Quotes')
    # files_in_basepath = basepath.iterdir()
    # for _, item in enumerate(files_in_basepath):
    #     qt.modify_quotes(item)

    # Removing the brackets from the modified fortune files, putting into one chunk of string.
    quotes = qt.remove_brackets(os.path.join(
        base_path, f'Mod_{fortune_file_path.name}'))
    # making a quotelist, without the brackets so its ready for subtitles search
    quote_list = qt.make_quote_list(quotes)
    # making a list of just the search terms
    quote_search_list = qt.make_quote_search_list(quote_list)
    # Extracting the frames from the timestamps we got before.
    im.extract_frames(base_path, quote_search_list)

    frames_path = Path(os.path.join(base_path, 'Frames'))
    files_in_frames = list(frames_path.iterdir())

    for _, item in enumerate(files_in_frames):
        if item.suffix == '.jpg':
            im.make_wallpapers(base_path, item, quote_list)

    shutil.rmtree(os.path.join(base_path, 'Frames'))
    os.remove(os.path.join(base_path, f'Mod_{fortune_file_path.name}'))


main()
