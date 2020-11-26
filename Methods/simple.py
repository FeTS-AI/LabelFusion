import numpy as np
from .majority_voting import *
from .utils import *

def simple_iterative(segmentationArray_oneHot):
  '''
  This function takes an list of one-hot encoded masks and returns a 3D one-hot encoded mask

  Reference: DOI:10.1109/tmi.2010.2057442
  '''
  segmentationArray_oneHot_wrap = segmentationArray_oneHot
  init_seg = majority_voting(segmentationArray_oneHot_wrap) # use majority voting as initial
  
  dice_list = []
  num_classes = segmentationArray_oneHot_wrap[0].shape[0]
  # calculate dice for each input compared to initial segmentation
  for i in range(0, len(segmentationArray_oneHot_wrap)): 
    dice_list.append(1 - MCD_loss(segmentationArray_oneHot_wrap[i], init_seg, num_classes))

  num_iter = len(segmentationArray_oneHot_wrap) - 1 # initialize the number of iterations

  seg_sum = segmentationArray_oneHot[0]
  for i in range(num_iter):
    order = np.array(dice_list).argsort() # sort the dice
    # remove the first segmentation because 
    del dice_list[order[0]] 
    del segmentationArray_oneHot_wrap[order[0]]

    dice_list = [] # re-initilize dice list to get iteratively updated 
    for i in range(0, len(segmentationArray_oneHot_wrap)): 
      current_dice = 1 - MCD_loss(segmentationArray_oneHot_wrap[i], init_seg, num_classes)
      dice_list.append(current_dice)
      seg_sum += current_dice * segmentationArray_oneHot_wrap[i]
    

  return init_seg