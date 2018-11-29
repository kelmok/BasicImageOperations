# downsampleEveryN.py
# takes input filename and 'downsamples' image by taking every Nth column and repeating it N times
# Author: kelvin.mok@mail.mcgill.ca

import numpy as np
import PIL.Image as Image

class downsampleEveryN:

  def __init__(self, filename_image, rate_N):
    self.filename   = filename_image
    self.image      = Image.open(filename)
    self.imgarr     = np.asarray(img,np.int)
    self.imgarr_ds  = imgarr(:,::rate_N)
    imgarr          = np.repeat(imgarr_ds,rate_N,1)
    imgout          = Image.fromarray(imgarr)
    return imgout
