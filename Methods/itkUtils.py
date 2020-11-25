import SimpleITK as sitk


def imageSanityCheck(targetImageFile, inputImageFile) -> bool:
  '''
  This function does sanity checking of 2 images
  '''
  targetImage = sitk.ReadImage(targetImageFile)
  inputImage = sitk.ReadImage(inputImageFile)

  if targetImage.GetDimension() != inputImage.GetDimension():
    print('Dimension mismatch for target and input image', file = sys.stderr)
    return False

  if targetImage.GetSize() != inputImage.GetSize():
    print('Size mismatch for target and input image', file = sys.stderr)
    return False
    
  if targetImage.GetOrigin() != inputImage.GetOrigin():
    print('Origin mismatch for target and input image', file = sys.stderr)
    return False

  if targetImage.GetSpacing() != inputImage.GetSpacing():
    print('Spacing mismatch for target and input image', file = sys.stderr)
    return False

  return True