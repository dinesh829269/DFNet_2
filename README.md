# Deep Fusion Network for Image completion

- Added loss functions.
- Added image metrics.

## Introduction

Examples of corresponding images:

![](imgs/github_teaser.jpg)

If you find this code useful for your research, please cite:

```
@inproceedings{xin2019dfnet,
  title={Deep Fusion Network for Image Completion},
  author={Xin Hong and Pengfei Xiong and Renhe Ji and Haoqiang Fan},
  journal={arXiv preprint},
  year={2019},
}
```

## Prerequisites

- Python 3
- PyTorch 1.0
- OpenCV

## Testing

Clone this repo:

``` py
git clone https://github.com/hughplay/DFNet.git
cd DFNet
```

Download pre-trained model from [Google Drive](https://drive.google.com/drive/folders/1lKJg__prvJTOdgmg9ZDF9II8B1C3YSkN?usp=sharing)
and put them into `model`.

### Testing with Places2 model

There are already some sample images in the `samples/places2` folder.

``` sh
python test.py --model model/model_places2.pth --img samples/places2/img --mask samples/places2/mask --output output/places2 --merge
```

### Testing with CelebA model

There are already some sample images in the `samples/celeba` folder.

``` sh
python test.py --model model/model_celeba.pth --img samples/celeba/img --mask samples/celeba/mask --output output/celeba --merge
```

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

