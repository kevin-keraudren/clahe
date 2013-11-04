#!/usr/bin/python

from lib.clahe import CLAHE
import numpy as np
import cv2

# CLAHE
img = cv2.imread( "nuclei.png", 0 ).astype('uint8')

for win in [2,5,20,50]:
    cv2.imwrite( "result_"+str(win)+".png", CLAHE( img, win, win, 128, 5 ) )

# Contrast stretch
img = cv2.imread( "nuclei.png", 0 ).astype('uint8')

img = img.astype('float')
img -= img.min()
img /= img.max()
img *= 255

cv2.imwrite( "contrast_stretched.png", img )
