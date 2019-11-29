#!/usr/bin/env python

##########################################################################
# Crear un tileset horizontal a partir de una secuencia de imagenes .pngs:

import sys, os, re
from PIL import Image

input_seq_format = "png"
type_input_img = "RGBA"
type_output_img = "RGBA"
output_tileset_file = "tileset.png"
out_format = "PNG"

# si existe ya el tileset lo borro:
if os.path.exists(output_tileset_file):
    os.remove(output_tileset_file)

images = []
for seq_img in os.listdir('.'):
    if re.match(r'.*\.' + input_seq_format, seq_img):
        im = Image.open(seq_img)
        if type_input_img == "RGBA":
            im = im.convert('RGBA')
        images.append(im)

widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

if type_output_img == "RGBA":
    new_im = Image.new('RGBA', (total_width, max_height))
else:
    new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0

for im in images:
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

new_im.save(output_tileset_file, out_format)
