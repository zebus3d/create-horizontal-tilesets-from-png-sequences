#!/usr/bin/env python

import os
import re

from PIL import Image

##########################################################################
# This script create a horizontal tileset from a sequence of images .pngs.
# This script must be executed next to the pngs sequence.
##########################################################################

'''
2019 Jorge Hernandez - Melendez
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

# Settings:
input_seq_format = "png"  # all png in current dir
type_input_img = "RGBA"
type_output_img = "RGBA"
output_tileset_file = "tileset-bunny.png"  # name of image result
out_format = "PNG"

# if there are a previous tileset, they will be removed:
if os.path.exists(output_tileset_file):
    os.remove(output_tileset_file)

images = []
for seq_img in sorted(os.listdir('.')):
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

# Create the output file:
# When optimize option is True
# compress_level has no effect (it is set to 9 regardless of a value passed).
# new_im.save(output_tileset_file, out_format, compress_level=9)
new_im.save(output_tileset_file, out_format, optimize=True)
