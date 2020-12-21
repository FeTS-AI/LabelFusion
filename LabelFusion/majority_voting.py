import numpy as np

def majority_voting(segmentationArray_oneHot):
  '''
  This function takes an list of one-hot encoded masks as input and returns a 3D one-hot encoded mask
  '''
  seg_sum = segmentationArray_oneHot[0] # initialize
  for i in range(1, len(segmentationArray_oneHot)): # add all of them up
    seg_sum += segmentationArray_oneHot[i]

  init_seg = (seg_sum/len(segmentationArray_oneHot)>(0.5)).astype(int) # Doing the majority voting and then round
  return init_seg