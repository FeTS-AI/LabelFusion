from .majority_voting import *

def fuse_segmentations(list_of_oneHotEncodedSegmentations, method: str):
  '''
  This function takes a list of one-hot encoded segmentations and the method as input and returns the one-hot encoded fused segmentation
  '''
  if 'majority' in method:
    return majority_voting(list_of_oneHotEncodedSegmentations)