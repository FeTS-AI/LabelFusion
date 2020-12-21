import numpy as np

def convert_to_3D(segmentation_oneHot, class_list):
  '''
  This function takes a one-hot encoded mask and the class list as input and returns a 3D segmentation
  '''
  returnSeg = segmentation_oneHot[class_list[0]] * class_list[0] # initialize
  for i in range(1, len(class_list)):
    returnSeg += segmentation_oneHot[i] * class_list[i]

  return returnSeg

def one_hot_nonoverlap(segmask_array, class_list):
  '''
  This function takes an N-D mask and a class list and returns a dictionary of one-hot encoded segmentations
  '''
  returnSeg = []
  for i in range(0, len(class_list)):
    returnSeg.append((segmask_array == class_list[i]).astype(np.uint8))

  return np.stack(returnSeg, axis=0)

def dice_loss(inp, target):
  '''
  This function calculates the DICE loss for 2 segmentation arrays
  '''
  smooth = 1e-7
  iflat = inp.flatten()
  tflat = target.flatten()
  intersection = (iflat * tflat).sum()
  return 1 - ((2. * intersection + smooth) /
              (iflat.sum() + tflat.sum() + smooth))

def MCD_loss(pm, gt, num_class):
  '''
  This function calculates the DICE loss for 2 multi-class segmentation arrays
  '''
  acc_dice_loss = 0
  for i in range(0,num_class):
      acc_dice_loss += dice_loss(gt[i,:,:,:],pm[i,:,:,:])
  acc_dice_loss/= num_class
  return acc_dice_loss