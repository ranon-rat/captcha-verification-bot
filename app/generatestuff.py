
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import Random, randint, choice
from math import sin, cos, pi
from io import BytesIO


class Generate:
    def __init__(self) -> None:
        self.fnt: ImageFont = ImageFont.truetype(
            'Arial Unicode.ttf', 30)  # the font
        self.img = Image.new("RGB", (300, 100), color=(
            randint(100, 255), randint(100, 255), randint(100, 255)))
        self.buff = BytesIO()  # the buffer image

    # generate the str

    def random_string(self) -> str:
        def random_char(): return choice(
            [chr(randint(65, 90)), chr(randint(97, 122)), chr(randint(48, 57))])
        return "".join([random_char() for i in range(10)])
    # this is only for manipulate the image

    def degenerate(self)->None:
        xsize, ysize = self.img.size

        for x in range(1, xsize):
            for y in range(1, ysize):

                self.img.putpixel(
                    (
                        int(x) % xsize,
                        int((sin(x)*10)*cos(y)*8) % ysize
                    ),
                    self.img.getpixel((x, y)))
    # it returns the value that the user need for been verified

    def generate_image(self) -> Tuple[str, BytesIO]:
        text = self.random_string()
        captcha: ImageDraw = ImageDraw.Draw(self.img)
        captcha.text((10, 30), text, fill=(40, 40, 40), font=self.fnt)

        self.degenerate()
       
        self.img.save(self.buff, format="PNG")

        return (text, self.buff)


Generate().generate_image()
