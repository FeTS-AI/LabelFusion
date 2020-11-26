import numpy as np
from .majority_voting import *
from .utils import *

def simple_iterative(segmentationArray_oneHot):
  '''
  This function takes an list of one-hot encoded masks and returns a 3D one-hot encoded mask
  '''
  init_seg = majority_voting(segmentationArray_oneHot) # use majority voting as initial
  
  dice_list = []
  num_classes = segmentationArray_oneHot[0].shape[0]
  # calculate dice for each input compared to initial segmentation
  for i in range(0, len(segmentationArray_oneHot)): 
    dice_list.append(1 - MCD_loss(segmentationArray_oneHot[i], init_seg, num_classes))

  num_iter = len(segmentationArray_oneHot) - 1 # initialize the number of iterations
  
  return init_seg