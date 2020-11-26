import SimpleITK as sitk

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
