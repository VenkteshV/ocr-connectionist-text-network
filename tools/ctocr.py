from PIL import Image, ImageOps
import subprocess, sys, os, glob
from time import sleep
DEMO_IMAGE_DIR="demo_images/"
def split_pdf(filename):
    prefix,postfix =filename.filename.split(".")
    print filename.filename
    print prefix
    cmd = "pdftoppm  %s  demo_images/%s" % (filename.filename, prefix)
    os.system(cmd)
    print (cmd)
    sleep(200)
    demo_imnames=os.listdir(DEMO_IMAGE_DIR)
    # subprocess.call([cmd], shell=True)
    print ("demo_images: %s"%demo_imnames)
    for im_name in demo_imnames:
        print ("Image: %s"%im_name)
        command = "unpaper -b 0.3 -mask-scan-maximum -mask-center -grayfilter-threshold -blurfilter -blackfilter-intensity -noisefilter --no-deskew --no-wipe -border -border-scan --no-border-align --overwrite -t ppm demo_images/%s demo_images/%s" % (im_name,im_name)
        sharpening = "convert demo_images/%s -sharpen 0x5 -colorspace Gray demo_images/%s" % (im_name,im_name)
        os.system(command)
        os.system(sharpening)
        print (command)
        print(sharpening)
    return [f for f in glob.glob(os.path.join('demo_images', '%s*' % prefix))]

def extract_pdf(filename):

    pngfiles = split_pdf(filename)
    sys.stderr.write("Pages: %d\n" % len(pngfiles))
