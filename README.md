# image_splicer

Image Splicer script written in Python. This script will read all images from the input directory, resize them to largest image dimensions and splice them together to form one image. The number of slices is a random generated number between MIN_SLICES and MAX_SLICES values. Splicing orientation can be set to either vertical or horizontal. You have the option of horizontal or vertical slicing and picking random slices or sequenced slicing.


#Usage
```
Image splicer

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_DIR, --input INPUT_DIR
                        input dir of source images
  -mn MIN_SLICES, --minslices MIN_SLICES
                        Minimum slices
  -mx MAX_SLICES, --maxslices MAX_SLICES
                        Max slices
  -r RANDOM_SPLICING, --random RANDOM_SPLICING
                        Random splicing
  -o {vertical,horizontal}, --orientation {vertical,horizontal}
                        Splice Orientation
```
