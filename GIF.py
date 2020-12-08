# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:09:11 2020

@author: cuimi
"""

import os
import imageio

png_dir = 'C:/Users/cuimi/OneDrive/桌面/gender/good_female/good_female'



images = []

for file_name in os.listdir(png_dir):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('C:/Users/cuimi/OneDrive/桌面/gender/good_female/good_female.gif', images)