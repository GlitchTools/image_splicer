# image_splicer

Image Splicer Script written in Python.
Just throw as many images as you want into your input directory of choice and the script
will resize all to largest image's dimenstions splicing them together to form one image.
You have the option of horizonal or vertical slicing and picking random slices or sequenced slicing.


#Usage
```
Image splicer

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_DIR, --input INPUT_DIR
                        input dir of source images
  -mn MIN_STRIPES, --minstripes MIN_STRIPES
                        Minimum Stripes
  -mx MAX_STRIPES, --maxstripes MAX_STRIPES
                        Max Stripes
  -r RANDOM_SPLICING, --random RANDOM_SPLICING
                        Random splicing
  -o {verticle,horizontal}, --orientation {verticle,horizontal}
                        Splice Orientation
```
