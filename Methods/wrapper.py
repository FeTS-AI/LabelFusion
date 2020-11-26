from .majority_voting import *
from .simple import *
from .staple import *

def fuse_segmentations(list_of_oneHotEncodedSegmentations, method, class_list):
  '''
  This function takes a list of one-hot encoded segmentations and the method as input and returns the one-hot encoded fused segmentation
  '''
  if 'majority' in method:
    return majority_voting(list_of_oneHotEncodedSegmentations)
  elif 'simple' in method:
    return simple_iterative(list_of_oneHotEncodedSegmentations)
  elif 'staple' in method:
    return staple(list_of_oneHotEncodedSegmentations, class_list)

  test = 1
