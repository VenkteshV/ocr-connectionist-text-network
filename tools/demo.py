
from cfg import Config as cfg
from other import draw_boxes, resize_im, CaffeModel
import cv2, os, caffe, sys
from detectors import TextProposalDetector, TextDetector
import os.path as osp
from utils.timer import Timer

DEMO_IMAGE_DIR="demo_images/"
NET_DEF_FILE="models/deploy.prototxt"
MODEL_FILE="models/ctpn_trained_model.caffemodel"

if len(sys.argv)>1 and sys.argv[1]=="--no-gpu":
    caffe.set_mode_cpu()
else:
    caffe.set_mode_gpu()
    caffe.set_device(cfg.TEST_GPU_ID)

# initialize the detectors
text_proposals_detector=TextProposalDetector(CaffeModel(NET_DEF_FILE, MODEL_FILE))
text_detector=TextDetector(text_proposals_detector)

demo_imnames=os.listdir(DEMO_IMAGE_DIR)
timer=Timer()
try:
    os.mkdir('boxes')
except:
    pass
box_count = 0
i = 0
for im_name in demo_imnames:
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("Image: %s"%im_name)

    im_file=osp.join(DEMO_IMAGE_DIR, im_name)
    im=cv2.imread(im_file)
    print ("shape",im.shape)
    timer.tic()

    im, f=resize_im(im, cfg.SCALE, cfg.MAX_SCALE)
    text_lines=text_detector.detect(im)

    print ("Number of the detected text lines: %s"%len(text_lines))
    print ("Time: %f"%timer.toc())

    im_with_text_lines,bboxes=draw_boxes(im, text_lines,i, caption=im_name, wait=False)
    i+=1
    for k in text_lines:
        top,left,bottom,right,score = k
        print score
        crop_img = im[int(left):int(right),int(top):int(bottom)]
        cv2.imwrite('boxes/box_{}.jpg'.format(box_count),crop_img)
        box_count += 1
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print bboxes
print ("Thank you for trying our demo. Press any key to exit...")
cv2.waitKey(0)
