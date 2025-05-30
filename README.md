# LabelFusion

<p align="center">
    <a href="https://github.com/FeTS-AI/LabelFusion/actions/workflows/test.yml"><img src="https://github.com/FeTS-AI/LabelFusion/actions/workflows/test.yml/badge.svg" alt="Build Status"></a>
    <a href="https://doi.org/10.5281/zenodo.4534122"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4534122.svg" alt="DOI"></a>
    <a href="https://anaconda.org/conda-forge/labelfusion" alt="Install"><img src="https://img.shields.io/conda/vn/conda-forge/labelfusion" /></a>
    <a href="https://pypi.org/project/LabelFusion/"><img src="https://img.shields.io/pypi/v/labelfusion"/></a>
</p>


This repo contains implementation of various label fusion approaches that can be used to fuse multiple labels.

## Installation

### Default
```sh
conda create -n venv_labelFusion python=3.12 -y
conda activate venv_labelFusion
pip install LabelFusion
```

### For Development
```sh
# fork to your own repo
git clone ${yourFork_labelFusion_repo_link}
cd LabelFusion
conda create -p ./venv python=3.12 -y
conda activate ./venv
pip install -e .
# develop, push
# initiate pull request
```

## Available fusion methods:

- [Voting (ITK)](https://simpleitk.org/doxygen/latest/html/classitk_1_1simple_1_1LabelVotingImageFilter.html): [DOI:10.1016/j.patrec.2005.03.017](https://doi.org/10.1016/j.patrec.2005.03.017)
- [STAPLE (ITK)](https://simpleitk.org/doxygen/latest/html/classitk_1_1simple_1_1MultiLabelSTAPLEImageFilter.html): [DOI:10.1109/TMI.2004.830803](https://doi.org/10.1109/TMI.2004.830803)
- Majority Voting: [DOI:10.1007/978-3-319-20801-5_11](https://doi.org/10.1007/978-3-319-20801-5_11)
- SIMPLE: [DOI:10.1109/tmi.2010.2057442](https://doi.org/10.1109/TMI.2010.2057442)

## Usage

### Command-Line interface

```sh
# continue from previous shell
python fusion_run -h
  -h, --help        show this help message and exit
  -inputs INPUTS    The absolute, comma-separated paths of labels that need to be fused
  -classes CLASSES  The expected labels; for example, for BraTS, this should be '0,1,2,3' - not used for STAPLE or ITKVoting
  -method METHOD    The method to apply; currently available: STAPLE | ITKVoting | MajorityVoting | SIMPLE
  -output OUTPUT    The output file to write the results
```

Example:
```sh
# continue from previous shell
python fusion_run \
-inputs /path/to/seg_algo_0.nii.gz,/path/to/seg_algo_1.nii.gz,/path/to/seg_algo_2.nii.gz \
-classes 0,1,2,3 \
-method STAPLE \
-output /path/to/seg_fusion.nii.gz
```

### Python interface

```python
# assuming virtual environment containing LabelFusion is activated
import SimpleITK as sitk
from LabelFusion.wrapper import fuse_images

label_to_fuse_0 = '/path/to/seg_algo_0.nii.gz'
label_to_fuse_1 = '/path/to/seg_algo_1.nii.gz'

images_to_fuse = []
images_to_fuse.append(sitk.ReadImage(label_to_fuse_0, sitk.sitkUInt8))
images_to_fuse.append(sitk.ReadImage(label_to_fuse_1, sitk.sitkUInt8))
fused_staple = fuse_images(images_to_fuse, 'staple') # class_list is not needed for staple/itkvoting
sitk.WriteImage(fused_staple, '/path/to/output_staple.nii.gz')
fused_simple = fuse_images(images_to_fuse, 'simple', class_list=[0,1,2,3])
sitk.WriteImage(fused_simple, '/path/to/output_simple.nii.gz')
```

## Testing

This repo has continuous integration enabled via [GitHub Actions](https://github.com/FeTS-AI/LabelFusion/actions/workflows/test.yml) for the following [operating systems](https://github.com/FeTS-AI/LabelFusion/blob/main/.github/workflows/test.yml#L18):

- Windows
- Ubuntu
- macOS

And for the following python versions:

- 3.9
- 3.10
- 3.11
- 3.12
