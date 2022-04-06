from PIL import Image, ImageDraw, ImageFont
import argparse
import os
import cv2
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('--font', '-f', type=str, default='./font.ttc')
parser.add_argument('--size', '-s', type=int, default=128)
parser.add_argument('--str', '-t', type=str, default='示例')
parser.add_argument('--outdir', '-o', type=str, default='./fontInput')
args = parser.parse_args()


def genFontImage(font, char):
    image = Image.new('1', (font.size, font.size), '#FFFFFF')
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), char, font=font, fill='#000000')
    return image


size = args.size
outdir = args.outdir
fontstr = args.str
fontPath = args.font
if not os.path.exists(outdir):
    os.mkdir(outdir)

font = ImageFont.truetype(fontPath, size)

for fontchar in fontstr:
    image = genFontImage(font, fontstr)
    image.save(os.path.join(outdir, f'{fontchar}.jpg'))
