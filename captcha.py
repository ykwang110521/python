#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image, ImageDraw, ImageFont
import string
import random


def generate_authenticode():
    # Generate random letters
    letters = ''.join([random.choice(string.ascii_letters) for i in range(4)])

    # Set the size of the image
    width = 100
    height = 40

    # Generate an image
    im = Image.new("RGB", (width, height), (255, 255, 255))

    # Draw letters on the image
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 30)
    for i in range(4):
        dr.text((5+i*20, 5), letters[i], (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), font)
    del dr

    # Change the background color
    for x in range(width):
        for y in range(height):
            if im.getpixel((x, y)) == (255, 255, 255):
                im.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    # Save the image
    im.save('t1.png')


generate_authenticode()