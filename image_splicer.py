# Written by stephen salmon
# email stephensalmon.mayo@gmail.com
# splices\stipes all the images in the input directory together

import PIL
from PIL import Image
import os
import random

input_dir = "/home/stephen.salmon/Pictures/image_stripes"
output_dir = "/home/stephen.salmon/Pictures/image_stripes/output/"
images = []
resized_images = []
largest_area = 0
largest_dims = ()
dims = []
image_formats = ['.jpg', '.jpeg', '.png', '.tif', '.bmp']
OUTPUT_FORMAT = '.tif'
show_image = True
random_source_coords = False
horizontal_striping = True
MIN_STRIPES = 40
MAX_STRIPES = 70
no_of_stripes = random.randint(MIN_STRIPES,MAX_STRIPES)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file in os.listdir(input_dir):
    filepath = os.path.join(input_dir, file)
    if os.path.isfile(filepath):
        if os.path.splitext(filepath)[1].lower() in image_formats:
            img = Image.open(filepath)
            images.append(img)
            h, w = img.size
            area = h * w
            if area > largest_area:
                largest_area = h * w
                largest_dims = h, w

width,height = largest_dims
mod_width = width % no_of_stripes
mod_height = height % no_of_stripes
if mod_width != 0:
    width = width - mod_width
if mod_height != 0:
    height = height - mod_height
largest_dims = width, height

for img in images:
    resized_img = img.resize(largest_dims, 3)
    resized_images.append(resized_img)

w, h = largest_dims
stripe_coords = ()
coords_list = []
if horizontal_striping:
    split = range(0, int(h), int(int(h) / int(no_of_stripes)))  # horizontal
    for coord in split:
        stripe_coords = (0, coord, w, int(coord + h / no_of_stripes))
        coords_list.append(stripe_coords)
else:
    split = range(0, int(w), int(int(w) / int(no_of_stripes)))
    for coord in split:
        stripe_coords = (coord, 0, int(coord + w / no_of_stripes), h)
        coords_list.append(stripe_coords)

stripe_image = Image.new('RGB',largest_dims)
for coords in coords_list:
    if random_source_coords:
        source_coords = coords_list[random.randint(0, len(coords_list)-1)]
    else:
        source_coords = coords
    stripe = resized_images[random.randint(0,len(resized_images)-1)].crop(source_coords)
    stripe_image.paste(stripe, coords)
random = str(random.randint(0, 100000))
image_name="image_striper"+random+OUTPUT_FORMAT
img_out= os.path.join(output_dir, image_name)
print("saving image to {0}".format(img_out))
stripe_image.save(img_out)
if show_image:
    stripe_image.show()


