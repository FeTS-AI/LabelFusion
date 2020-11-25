import numpy as np

def convert_to_3D(seg, class_list):
  '''
  This function takes a one-hot encoded mask and returns a 3D segmentation
  '''
  returnSeg = seg[class_list[0]] * class_list[0]
  for i in range(1, len(class_list)):
    returnSeg += seg[i] * class_list[i]

  return returnSeg

def one_hot_nonoverlap(segmask_array, class_list):
  '''
  This function takes an N-D mask and a class list and returns a dictionary of one-hot encoded segmentations
  '''
  returnSeg[class_list[0]] = (segmask_array == class_list[0]).astype(np.uint8)
  for i in range(1, len(class_list)):
    returnSeg[class_list[i]] = (segmask_array == class_list[i]).astype(np.uint8)

  return np.array(onehot_stack)
    
def one_hot_2_overlap(segmask_array):
    wht_mask = (segmask_array >= 1).astype(np.uint8)
    tuc_mask = np.logical_or(segmask_array == 1, segmask_array == 4)
    tuc_mask = tuc_mask.astype(np.uint8)
    enh_mask = (segmask_array == 4).astype(np.uint8)
    onehot_stack = [wht_mask, tuc_mask, enh_mask]
    return np.array(onehot_stack)
