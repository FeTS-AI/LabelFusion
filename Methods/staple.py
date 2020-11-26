import SimpleITK as sitk
from .utils import *

def staple(segmentationArray_oneHot, class_list_int):
  '''
  This function takes an list of one-hot encoded masks and class list as inputs and returns a 3D one-hot encoded mask

  Reference: DOI:10.1007/3-540-45786-0_37
  '''
  segmentation_images = []
  for i in range(0, len(segmentationArray_oneHot)):
    currentImage_fused = convert_to_3D(segmentationArray_oneHot[i], class_list_int)
    currentImage = sitk.GetImageFromArray(currentImage_fused)
    segmentation_images.append(currentImage)

  fused_segmentation = sitk.MultiLabelSTAPLE(segmentation_images)

  return fused_segmentation