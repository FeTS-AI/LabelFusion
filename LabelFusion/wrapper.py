from .fusion_wrappers import *


def fuse_images(list_of_simpleITK_images, method, class_list=None):
    """
    This function takes a list of simpleITK images and pushes it to appropriate functions
    """

    method = method.lower()

    if not (
        method in direct_itk_LabelFusion
    ):  # for non-itk LabelFusion, get image arrays
        inputListOfOneHotEncodedMasks = []

        for image in list_of_simpleITK_images:
            current_immage_array = sitk.GetArrayFromImage(
                image
            )  # initialize the fused segmentation array

            inputListOfOneHotEncodedMasks.append(
                one_hot_nonoverlap(current_immage_array, class_list)
            )

        # call the fusion
        fused_oneHot = fuse_segmentations_nonITK(
            inputListOfOneHotEncodedMasks, method, class_list
        )
        fused_segmentation_image = sitk.GetImageFromArray(
            convert_to_3D(fused_oneHot, class_list)
        )
        fused_segmentation_image.CopyInformation(list_of_simpleITK_images[0])

    else:  # for direct itk LabelFusion, we actually need the images themselves
        # call the fusion
        fused_segmentation_image = fuse_segmentations_itk(
            list_of_simpleITK_images, method
        )

    return fused_segmentation_image
