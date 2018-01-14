from PIL import Image, ImageOps
import subprocess, sys, os, glob

def split_pdf(filename):

    prefix,postfix =filename.filename.split(".")
    print filename.filename
    print prefix
    cmd = "pdftoppm -png %s  demo_images/%s" % (filename.filename, prefix)
    # subprocess.call([cmd], shell=True)
    os.system(cmd)
    print (cmd)
    return [f for f in glob.glob(os.path.join('demo_images', '%s*' % prefix))]

def extract_pdf(filename):

    pngfiles = split_pdf(filename)
    sys.stderr.write("Pages: %d\n" % len(pngfiles))
