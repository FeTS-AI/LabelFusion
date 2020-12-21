import SimpleITK as sitk
import sys

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

def imageComparision(targetImageFile, inputImageFile) -> bool:
  '''
  This function compares arrays of 2 images
  '''
  if imageSanityCheck(targetImageFile, inputImageFile): # proceed only when sanity check passes
    target_array = sitk.GetArrayFromImage(sitk.ReadImage(targetImageFile))
    input_array = sitk.GetArrayFromImage(sitk.ReadImage(inputImageFile))

    if (target_array == input_array).all():
      return True

  return False