# -*- coding: utf-8 -*-
#!/usr/bin/env python2

import os

input_dir = r'/home/narwhale/Maps/DATA/input/' # in Windows: input_dir = r'D:\data\input'
output_dir = r'/home/narwhale/Maps/DATA/output/' # in Windows: output_dir = r'D:\data\output'
for filename in os.listdir(input_dir):
    input_file = os.path.join(input_dir, filename)
    output_file = os.path.join(output_dir, filename)
     # Здесь делаем что-нибудь с input_file и output_file
     
      
