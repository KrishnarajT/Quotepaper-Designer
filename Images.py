from PIL import ImageFont, ImageDraw, Image, ImageEnhance, ImageFilter
from pathlib import Path
import Subtitle as sb
import cv2
import os

# Defining some fonts
ttf_poiret_one = ImageFont.truetype('./Fonts/poiretone-regular.ttf', 40)
ttf_museo = ImageFont.truetype('./Fonts/Museo 300.otf', 40)
ttf_bariol = ImageFont.truetype('./Fonts/Bariol_Serif_Regular.otf', 40)
ttf_open = ImageFont.truetype('./Fonts/OpenSans-Regular.ttf', 40)

# Starting point of Y axis for the quotes beginning from top left, determines where the quotes begin from
# This variable depends on the number of lines in the quotes that were allowed.

begin_y = 600
begin_x = 80


def extract_frames(path_to_folder, quote_search_text):
    '''
    Extracts the frame from the video and the subtitle, and saves them in the frames folder
    The names of the frames are just the names of the quote_search_text list's index so
    we know what texts hit and what didnt hit in the subtitle file.
    '''
    basepath = Path(path_to_folder)
    files_in_basepath = list(basepath.iterdir())

    for h, k in enumerate(quote_search_text):
        for _, item in enumerate(files_in_basepath):
            found = 0
            if item.suffix == '.srt':
                path_to_vid = str(item).strip('.srt') + '.mkv'
                found = sb.search_in_srt(item, k)

                with open(item, 'r', errors='ignore') as f:
                    all_subs = f.readlines()

                    if found:
                        timestamp = sb.find_timestamp(all_subs, found)
                        if timestamp == []:
                            break
                        print(timestamp)

                        video = cv2.VideoCapture(path_to_vid)
                        fps = video.get(cv2.CAP_PROP_FPS)
                        fps = round(fps, 2)
                        print(fps)

                        frame_no = round(
                            ((timestamp[0] * 60 + timestamp[1]) * 60 + timestamp[2]) * fps + (timestamp[3]/1000) * fps)
                        print(frame_no)
                        video.set(1, frame_no)
                        success, image = video.read()
                        try:
                            cv2.imwrite(os.path.join(
                                path_to_folder, f"Frames/{h}.jpg"), image)
                        except:
                            print('some error')
                        break


def make_wallpapers(base_path, image_path, quote_list):
    # read the image
    im = Image.open(image_path)
    ov = Image.open("overlay.png")

    # image brightness enhancer
    img = im.resize((1920, 1080))

    enhancer = ImageEnhance.Sharpness(img)
    factor = 0.7  # decrease sharpness
    img = enhancer.enhance(factor)

    enhancer = ImageEnhance.Contrast(img)
    factor = 0.7  # decrease constrast
    img = enhancer.enhance(factor)

    img.paste(ov, (0, 0), mask=ov)
    # im_output = im_output.filter(ImageFilter.GaussianBlur(radius = 2))

    draw = ImageDraw.Draw(img)
    text = quote_list[int(image_path.stem)]
    draw.text((begin_x, begin_y), text, '#e1ebec',
              font=ttf_museo, align='left')
    img.save(f'./Wallpapers/{base_path.name} - {image_path.name}')
