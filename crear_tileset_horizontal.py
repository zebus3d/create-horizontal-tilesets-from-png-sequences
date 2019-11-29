#!/usr/bin/env python

import os
import re

from PIL import Image

##########################################################################
# Crear un tileset horizontal a partir de una secuencia de imagenes .pngs.
# Hay que ejecutar este script junto a la secuencia de pngs.
##########################################################################

# Settings:
input_seq_format = "png"  # all png in current dir
type_input_img = "RGBA"
type_output_img = "RGBA"
output_tileset_file = "tileset.png"  # name of image result
out_format = "PNG"

# if there are previous tiles, they will be removed:
if os.path.exists(output_tileset_file):
    os.remove(output_tileset_file)

images = []
for seq_img in os.listdir('.'):
    if re.match(r'.*\.' + input_seq_format, seq_img):
        im = Image.open(seq_img)
        if type_input_img == "RGBA":
            im = im.convert(type_input_img)
        images.append(im)

widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

if type_output_img == "RGBA":
    new_im = Image.new(type_output_img, (total_width, max_height))
else:
    new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0

for im in images:
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

# create the output file:
new_im.save(output_tileset_file, out_format)
