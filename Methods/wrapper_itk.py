import SimpleITK as sitk

def fuse_segmentations_itk(list_of_segmentations_images, method):
  '''
  This function takes a list of segmentations images and the method as input and returns the fused segmentation for ITK implementations
  '''
  if 'staple' in method:
    return sitk.MultiLabelSTAPLE(list_of_segmentations_images)
  elif 'voting' in method:
    return sitk.LabelVotingImageFilter(list_of_segmentations_images)
