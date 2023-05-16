import time
from smiley import Smiley


class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyebrows()
        self.draw_eyes()
        

    def draw_mouth(self):
        """
        Method that draws an angry mouth on the standard faceless smiley.
        """
        mouth = [43, 44, 50, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyebrows(self):
        """
        Method that draws the angry eyebrows on the standard faceless smiley.
        """
        eyebrows = [9, 14, 17, 18, 19, 20, 21, 22]
        for pixel in eyebrows:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        eyes = [26, 29]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def blink(self, delay=0.25):
        """
        Make the angry smiley blink once with a certain delay (in s).

        :param delay: Delay in seconds
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
