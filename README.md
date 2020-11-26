# LabelFusion
This repo contains implementation of various label fusion approaches that can be used to fuse multiple labels.

## Installation

```powershell
git clone ${labelFusion_repo_link}
cd LabelFusion
conda create -p ./venv python=3.6.5 -y
conda activate ./venv
pip install -e .
```

## Usage

```powershell
python ./fusion_run -h
  -h, --help        show this help message and exit
  -inputs INPUTS    The absolute, comma-separated paths of labels that need to be fused
  -classes CLASSES  The expected labels; for example, for BraTS, this should be '0,1,2,4'
  -method METHOD    The method to apply; currently available: STAPLE | ITKVoting | MajorityVoting | SIMPLE
  -output OUTPUT    The output file to write the results
```

Example:
```powershell
python ./fusion_run -inputs /path/to/seg_algo_1.nii.gz,/path/to/seg_algo_2.nii.gz,/path/to/seg_algo_3.nii.gz -classes 0,1,2,4 -method STAPLE -output /path/to/seg_fusion.nii.gz
```