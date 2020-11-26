from .majority_voting import *
from .simple import *
from .staple import *

def fuse_segmentations(list_of_oneHotEncodedSegmentations, method, class_list):
  '''
  This function takes a list of one-hot encoded segmentations and the method as input and returns the one-hot encoded fused segmentation for non-ITK implementations
  '''
  if 'majority' in method:
    return majority_voting(list_of_oneHotEncodedSegmentations)
  elif 'simple' in method:
    return simple_iterative(list_of_oneHotEncodedSegmentations)

  test = 1
