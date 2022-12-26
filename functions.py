from PIL import Image, ImageDraw

import os

def prepare_mask(size, antialias=2):
    mask = Image.new('L', (size[0] * antialias, size[1] * antialias), 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
    return mask.resize(size, Image.ANTIALIAS)


def crop(im, s):
    w, h = im.size
    k = w / s[0] - h / s[1]
    if k > 0:
        im = im.crop(((w - h) / 2, 0, (w + h) / 2, h))
    elif k < 0:
        im = im.crop((0, (h - w) / 2, w, (h + w) / 2))
    return im.resize(s, Image.ANTIALIAS)


def create_rounded_image(img):
    im = Image.open(img)
    round_radius = min(im.size)
    im = crop(im, (round_radius, round_radius))
    im.putalpha(prepare_mask((round_radius, round_radius), 4))
    output = str(img).rsplit('.', 1)[0] + ".png"

    try:
        im.save(output)
        print(f"[INFO] Photo saved successfully [{output}]")
    except:
        print(f"[INFO] Error saving photo [{output}]")
