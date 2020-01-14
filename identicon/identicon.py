#!/usr/bin/env python3
import hashlib

import pandas as pd
import numpy as np

from PIL import Image, ImageDraw

import os
import sys

from utilities import Utilities

class Identicon():
    
    def __init__(self):
        pass
        

    @staticmethod
    def do_something3(num1):
        '''
        This do_something3(num1) function is here to try and see 
        if the parameter comes from web servis is passing to 
        any function of Identicon class
        ''' 
        num1 = int(num1)
        num2 = (num1)*5
        df = pd.DataFrame(np.random.randn(num2,num1))
        df = df.to_json()
        function_output = df
        return function_output 
        

    @staticmethod
    def image_to_file(text):
        '''
        image_to_file function uses functions from utilitiesd module to generate
        an identicon and write to a folder named output with png extension
        '''
        
        text = text
        md5hash = hashlib.md5(text.encode('utf8')).hexdigest()
        hex_color = md5hash[:6]
        matrix = list()
        grid_size = 5
        for i in range(grid_size):
            array = list()
            for j in range(grid_size):
                c = i * grid_size + j + 6
                b = int(md5hash[c], base=16) % 2 == 0
                array.append(b)
            matrix.append(array)

        identicon = Utilities.draw_image(matrix, hex_color, True)
            
        #if not os.path.exists(output):
        #    os.mkdir(output)

        file_name = text.replace(' ', '-') + ".png"
        file_path = "{0}{1}{2}".format('output/', os.sep, file_name)
    
        identicon.save(file_path, "PNG")
            


    @staticmethod
    def generate_identicon(text):
        '''
        generate_identicon function uses functions from utilitiesd 
        module to generate an identicon and and return it
        '''
       
        text = text
        md5hash = hashlib.md5(text.encode('utf8')).hexdigest()
        hex_color = md5hash[:6]
        matrix = list()
        grid_size = 5
        for i in range(grid_size):
            array = list()
            for j in range(grid_size):
                c = i * grid_size + j + 6
                b = int(md5hash[c], base=16) % 2 == 0
                array.append(b)
            matrix.append(array)

        identicon = Utilities.draw_image(matrix, hex_color, True)
            
        return identicon
