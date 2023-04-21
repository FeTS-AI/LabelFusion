import SimpleITK as sitk
import sys


def imageSanityCheck(targetImageFile, inputImageFile) -> bool:
    """
    This function does sanity checking of 2 images
    """
    targetImage = sitk.ReadImage(targetImageFile)
    inputImage = sitk.ReadImage(inputImageFile)

    commonMessage = (
        " mismatch for target image, '"
        + targetImageFile
        + "' and input image, '"
        + inputImageFile
        + "'"
    )
    problemsIn = ""
    returnTrue = True

    if targetImage.GetDimension() != inputImage.GetDimension():
        problemsIn += "Dimension"
        returnTrue = False

    if targetImage.GetSize() != inputImage.GetSize():
        if not problemsIn:
            problemsIn += "Size"
        else:
            problemsIn += ", Size"
        returnTrue = False

    if targetImage.GetOrigin() != inputImage.GetOrigin():
        if not problemsIn:
            problemsIn += "Origin"
        else:
            problemsIn += ", Origin"
        returnTrue = False

    if targetImage.GetSpacing() != inputImage.GetSpacing():
        if not problemsIn:
            problemsIn += "Spacing"
        else:
            problemsIn += ", Spacing"
        returnTrue = False

    if returnTrue:
        return True
    else:
        print(problemsIn + commonMessage, file=sys.stderr)
        return False


def imageComparision(targetImageFile, inputImageFile) -> bool:
    """
    This function compares arrays of 2 images
    """
    if imageSanityCheck(
        targetImageFile, inputImageFile
    ):  # proceed only when sanity check passes
        target_array = sitk.GetArrayFromImage(sitk.ReadImage(targetImageFile))
        input_array = sitk.GetArrayFromImage(sitk.ReadImage(inputImageFile))

        if (target_array == input_array).all():
            return True

    return False
