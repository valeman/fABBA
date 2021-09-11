#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# load demo image samples

import os
import requests
import matplotlib.pyplot as plt
import sys

def get_img(file, store_dir):
    url_parent = "https://raw.githubusercontent.com/umtsd/C_temp_img/main/Stanford%20Dogs%20Dataset/"
    img_data = requests.get(url_parent + file).content
    with open(store_dir + "/" + file, 'wb') as handler:
        handler.write(img_data)
        
def load_images():
    samples_list = [ 'n02086646_2069.jpg',
                     'n02088094_3593.jpg',
                     'n02089078_2021.jpg',
                     'n02090379_2083.jpg',
                     'n02091134_14363.jpg',
                     'n02091134_17788.jpg',
                     'n02093428_17280.jpg',
                     'n02093428_1746.jpg',
                     'n02093428_1767.jpg',
                     'n02093428_19443.jpg',
                     'n02093859_2579.jpg',
                     'n02096585_2947.jpg',
                     'n02099601_5857.jpg',
                     'n02101556_4241.jpg',
                     'n02101556_8093.jpg',
                     'n02101556_8168.jpg',
                     'n02107312_5862.jpg',
                     'n02107683_5115.jpg',
                     'n02109525_6019.jpg',
                     'n02110063_1034.jpg',
                     'n02110185_3406.jpg',
                     'n02112706_637.jpg',
                     'n02113023_1825.jpg',
                     'n02115913_4117.jpg'
                   ]
    
    store_dir = "samples/img"
    
    if not os.path.isdir(store_dir):
        os.makedirs(store_dir)
        sys.stdout.write("Progress: [ %s" % ("" * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1)) 

        for img in samples_list:
            get_img(img, store_dir)
            sys.stdout.write("=")
            sys.stdout.flush()
        sys.stdout.write("]\n") 
        
    images = list()
    figs = os.listdir(store_dir)
    for filename in figs:
        img = plt.imread(os.path.join(store_dir,filename)) 
        if img is not None:
            images.append(img)
    return images