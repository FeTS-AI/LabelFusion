from .majority_voting import *
from .simple import *

import SimpleITK as sitk

direct_itk_LabelFusion = ['staple', 'itkvoting'] # variable that checks which LabelFusion can directly use itk images 

def fuse_segmentations_nonITK(list_of_oneHotEncodedSegmentations, method, class_list):
  '''
  This function takes a list of one-hot encoded segmentations and the method as input and returns the one-hot encoded fused segmentation for non-ITK implementations
  '''
  if 'majority' in method:
    return majority_voting(list_of_oneHotEncodedSegmentations)
  elif 'simple' in method:
    return simple_iterative(list_of_oneHotEncodedSegmentations)

def fuse_segmentations_itk(list_of_segmentations_images, method):
  '''
  This function takes a list of segmentations images and the method as input and returns the fused segmentation for ITK implementations
  '''
  if 'staple' in method:
    return sitk.MultiLabelSTAPLE(list_of_segmentations_images) # DOI: 10.1109/TMI.2004.830803
  elif 'voting' in method:
    votingFilter = sitk.LabelVotingImageFilter()
    votingFilter.SetLabelForUndecidedPixels(0)
    return votingFilter.Execute(list_of_segmentations_images) # DOI: 10.1016/j.patrec.2005.03.017
