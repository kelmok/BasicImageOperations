# downsampleEveryN.py
# takes input filename and 'downsamples' by repeating cols
# Author: kelvin.mok@mail.mcgill.ca
import numpy as np
import PIL.Image as Image

class downsampleEveryN():
  def __init__(self, filename_image, filename_imgout, rate_N):
    self.filename   = filename_image
    self.image      = Image.open(self.filename)
    imgarr          = np.asarray(self.image,np.int)
    imgarr_ds       = np.copy(imgarr[:,::rate_N])
    imgarr          = np.repeat(imgarr_ds,rate_N,1)
    imgds           = Image.fromarray(np.array(np.uint8(imgarr)))
    imgds.save(filename_imgout,"tiff")

