import numpy as np
from .majority_voting import *
from .utils import *

def simple_iterative(segmentationArray_oneHot):
  '''
  This function takes an list of one-hot encoded masks as input and returns a 3D one-hot encoded mask

  Reference: DOI:10.1109/tmi.2010.2057442
  '''
  segmentationArray_oneHot_wrap = segmentationArray_oneHot # make a copy so that input isn't overwritten
  seg_for_comparision = majority_voting(segmentationArray_oneHot_wrap) # use majority voting as initial
  
  dice_list = []
  num_classes = segmentationArray_oneHot_wrap[0].shape[0]
  # calculate dice for each input compared to initial segmentation
  for i in range(0, len(segmentationArray_oneHot_wrap)): 
    dice_list.append(1 - MCD_loss(segmentationArray_oneHot_wrap[i], seg_for_comparision, num_classes))

  num_iter = len(segmentationArray_oneHot_wrap) - 1 # initialize the number of iterations

  for i in range(num_iter):
    order = np.array(dice_list).argsort() # sort the dice
    # remove the best segmentation from comparision - part of SIMPLE algorithm
    del dice_list[order[0]] 
    del segmentationArray_oneHot_wrap[order[0]]

    dice_list = [] # re-initilize dice list to get iteratively updated 
    seg_sum = np.zeros(segmentationArray_oneHot[0].shape) # initialize the first segmentation
    # loop through remaining and calculate updated segmentation
    for i in range(0, len(segmentationArray_oneHot_wrap)): 
      current_dice = 1 - MCD_loss(segmentationArray_oneHot_wrap[i], seg_for_comparision, num_classes)
      dice_list.append(current_dice)
      seg_sum += current_dice * segmentationArray_oneHot_wrap[i]

    seg_for_comparision = (seg_sum/(sum(dice_list))>0.5).astype(int) # update the seg_for_comparision    

  return seg_for_comparision
