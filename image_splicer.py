# Written by stephen salmon
# email stephensalmon.mayo@gmail.com
# splices\stripes all the images in the input directory together

from PIL import Image
import os
import random
import argparse
import sys
import binascii

image_formats = ['.jpg', '.jpeg', '.png', '.tif', '.bmp', 'gif', 'tiff']
OUTPUT_FORMAT = '.png'
SAVE_IMAGE = True


def splice_images(images, min_stripes=20, max_stripes=200, orientation="verticle", random_coords=False):
    max_area = 0
    no_of_stripes = random.randint(min_stripes, max_stripes)
    # Get the largest dims
    for image in images:
        w, h = image.size
        area = h * w
        if area > max_area:
            max_area = area
            max_width, max_height = w, h
    max_width = max_width - (max_width % no_of_stripes)
    max_height = max_height - (max_height % no_of_stripes)

    output_image = Image.new('RGB', (max_width, max_height))
    # Resize all to the largest dimensions
    resized_images = []
    for image in images:
        resized_image = image.resize((max_width, max_height), 3)
        resized_images.append(resized_image)

    coords_list = []
    if orientation == "verticle":
        split = range(0, int(w), int(int(w) / int(no_of_stripes)))
        for coord in split:
            stripe_coords = (coord, 0, int(coord + w / no_of_stripes), h)
            coords_list.append(stripe_coords)
    else: # horizontal
        split = range(0, int(h), int(int(h) / int(no_of_stripes)))
        for coord in split:
            stripe_coords = (0, coord, w, int(coord + h / no_of_stripes))
            coords_list.append(stripe_coords)

    for coords in coords_list:
        if random_coords:
            source_coords = coords_list[random.randint(0, len(coords_list) - 1)]
        else:
            source_coords = coords
        stripe = resized_images[random.randint(0, len(resized_images) - 1)].crop(source_coords)
        output_image.paste(stripe, coords)
    return output_image


def get_all_images_from_the_input_dir(input_dir):
    images = []
    for file in os.listdir(input_dir):
        filepath = os.path.join(input_dir, file)
        if os.path.isfile(filepath):
            if os.path.splitext(filepath)[1].lower() in image_formats:
                img = Image.open(filepath)
                images.append(img)
    return images


def save_image(image):
    random_hash = str(binascii.b2a_hex(os.urandom(15)))[2:-1]
    output_image_name = "image_splicer" + random_hash + "_" + OUTPUT_FORMAT
    output_dir = "output"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir_path = os.path.join(script_dir, output_dir)
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    image_path = os.path.join(output_dir_path, output_image_name)
    print("Image saved to {0}".format(image_path))
    image.save(image_path)


def main():
    images = get_all_images_from_the_input_dir(INPUT_DIR)
    spliced_image = splice_images(images, MIN_STRIPES, MAX_STRIPES, orientation=ORIENTATION)
    spliced_image.show()
    if SAVE_IMAGE:
        save_image(spliced_image)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image splicer')
    parser.add_argument("-i", "--input", dest="INPUT_DIR",
                        default="/home/stephen.salmon/Pictures/sunsets",
                        help="input dir of source images")
    parser.add_argument("-mn", "--minstripes", dest="MIN_STRIPES", default=20, type=int, help="Minimum Stripes")
    parser.add_argument("-mx", "--maxstripes", dest="MAX_STRIPES", default=200, type=int, help="Max Stripes")
    parser.add_argument("-r", "--random", dest="RANDOM_SPLICING", default=False, help="Random splicing")
    parser.add_argument("-o", "--orientation", dest="ORIENTATION", default='horizontal',
                        choices=['verticle', 'horizontal'], help="Splice Orientation")
    try:
        args = parser.parse_args()
    except:
        print("Args Error")
        parser.print_help()
        sys.exit(2)
    if args.MIN_STRIPES:
        MIN_STRIPES = args.MIN_STRIPES
    if args.MAX_STRIPES:
        MAX_STRIPES = args.MAX_STRIPES
    if args.RANDOM_SPLICING:
        RANDOM_SPLICING = True
    if args.ORIENTATION:
        ORIENTATION = args.ORIENTATION
    if args.INPUT_DIR:
        if os.path.isdir(args.INPUT_DIR):
            INPUT_DIR = args.INPUT_DIR
        else:
            print("{0} is not a valid input directory".format(args.INPUT_DIR))
            parser.print_help()
            sys.exit(2)
    main()
