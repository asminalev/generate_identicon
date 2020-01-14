#!/usr/bin/env python3
import sys
import os
import argparse
import hashlib

from PIL import Image, ImageDraw



class Utilities():
    
    def __init__(self):
        pass

    @staticmethod
    def hex_to_rgb(hex_color):
        """
        Converts a 6 digit hex number to RGB.
        @param: hex_color - A 6 digit string with values in the range [a-fA-F0-9].
        @return: a tuple containing 3 integers.
        """
        if not isinstance(hex_color, str):
            raise TypeError("'hex_color' must be of type 'str'.")
        if len(hex_color) != 6:
            raise ValueError("'hex_color' must 6 characters in length (excluding '#') e.g. FF1919.")

        r = int(hex_color[0:2], base=16) 
        g = int(hex_color[2:4], base=16)
        b = int(hex_color[4:6], base=16)

        return (r,g,b)
    
    
    @staticmethod
    def draw_image(matrix, hex_color, symmetrical):
        """
        Renders an image were certain pixels are turned colored.
        @param: matrix      - A list of lists containing bools i.e. [[True, False, False, ...], [...], ...]
        @param: hex_color   - The color of each pixel.
        @param: symmetrical - whether the image should be symmetrical.
        
        @return: PIL.Image.Image object.
        """
        SQUARE    = 50 
        size      = (5 * SQUARE, 5 * SQUARE)  
        bg_color  = (214,214,214)
        pixel_on  = Utilities.hex_to_rgb(hex_color)
        
        if symmetrical:
            for i in range(5):
                matrix[i][4] = matrix[i][0]
                matrix[i][3] = matrix[i][1]
            
        image = Image.new("RGB", size, bg_color)
        draw  = ImageDraw.Draw(image)

        for x in range(5):
            for y in range(5):
                if matrix[x][y]:
                    bounding_box = [y * SQUARE, x * SQUARE, y * SQUARE + SQUARE, x * SQUARE + SQUARE]
                    draw.rectangle(bounding_box, fill=pixel_on)
        del(draw)
        return image

