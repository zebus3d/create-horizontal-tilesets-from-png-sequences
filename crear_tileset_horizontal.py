## crear tileset horizontal desde una secuencia de pngs:

import sys, os, re
from PIL import Image

sequence_format = "png"

outfile = "tileset.png"
out_format = "PNG"

# si existe ya el tileset lo borro:
if os.path.exists(outfile):
    os.remove(outfile)

# images = [Image.open(x) for x in ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']]
# images = [Image.open(seq_img) for seq_img in os.listdir('.') if re.match(r'.*\.' + sequence_format, seq_img)]

images = []
for seq_img in os.listdir('.'):
    if re.match(r'.*\.' + sequence_format, seq_img):
        im = Image.open(seq_img)
        im = im.convert('RGBA')
        images.append(im)

widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGBA', (total_width, max_height))

x_offset = 0

for im in images:
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

# new_im.save('tileset.jpg')
new_im.save(outfile, out_format)
