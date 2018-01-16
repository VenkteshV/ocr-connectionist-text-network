from PIL import Image, ImageOps
import subprocess, sys, os, glob
DEMO_IMAGE_DIR="demo_images/"
def split_pdf(filename):
    demo_imnames=os.listdir(DEMO_IMAGE_DIR)
    prefix,postfix =filename.filename.split(".")
    print filename.filename
    print prefix
    cmd = "pdftoppm  %s  demo_images/%s" % (filename.filename, prefix)
    os.system(cmd)
    print (cmd)
    # subprocess.call([cmd], shell=True)
    for im_name in demo_imnames:
        command = "unpaper -b 0.3 -mask-scan-maximum -mask-center -grayfilter-threshold -blurfilter -blackfilter-intensity -noisefilter --no-deskew --no-wipe -border -border-scan --no-border-align --overwrite -t ppm demo_images/%s demo_images/%s" % (im_name,im_name)
        os.system(command)
    print (command)
    return [f for f in glob.glob(os.path.join('demo_images', '%s*' % prefix))]

def extract_pdf(filename):

    pngfiles = split_pdf(filename)
    sys.stderr.write("Pages: %d\n" % len(pngfiles))
