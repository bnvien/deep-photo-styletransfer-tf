# An application of Deep Photo Style Transfer in Interior Design

This project aims to apply [Deep Photo Styletransfer](https://arxiv.org/abs/1703.07511) in developing an app that helps users apply the style from a sample image to the image of their house so that they can imagine how their house interior would look like after renovation. The source code is based on a [Tensorflow implementation](https://github.com/LouieYang/deep-photo-styletransfer-tf) of Deep Photo Styletransfer by Yang Liu.

<p align="center">
    <img src="./examples/readme_examples/Case6.png" width="712"/>
</p>

## Disclaimer
**This software is published for academic and non-commercial use only.**

## Setup
### Dependencies
* [Tensorflow](https://www.tensorflow.org/)
* [Numpy](www.numpy.org/)
* [Pillow](https://pypi.python.org/pypi/Pillow/)
* [Scipy](https://www.scipy.org/)
* [PyCUDA](https://pypi.python.org/pypi/pycuda) (used in smooth local affine)

***It is recommended to run the code on Google Colab, since you only need to install PyCUDA manually to setup. Check the provided Jupyter Notebook for a demo.***

### Download the VGG-19 model weights
The VGG-19 model of tensorflow is adopted from [VGG Tensorflow](https://github.com/machrisaa/tensorflow-vgg) with few modifications on the class interface. The VGG-19 model weights is stored as .npy file and could be download from [Google Drive](https://drive.google.com/file/d/0BxvKyd83BJjYY01PYi1XQjB5R0E/view?usp=sharing) or [BaiduYun Pan](https://pan.baidu.com/s/1o9weflK). After downloading, copy the weight file to the **./vgg19** directory

## Usage
### Basic Usage
You need to specify the path of content image, style image, content image segmentation, style image segmentation and then run the command

```
python deep_photostyle.py --content_image_path <path_to_content_image> --style_image_path <path_to_style_image> --content_seg_path <path_to_content_segmentation> --style_seg_path <path_to_style_segmentation> --style_option 0
```

*Example:*
```
python deep_photostyle.py --content_image_path ./examples/input/input.jpg --style_image_path ./examples/style/case6.jpg --content_seg_path ./examples/segmentation/input_mask.jpg --style_seg_path ./examples/segmentation/case6_mask.jpg --style_option 0 --max_iter 2000 --apply_smooth False --init_image_path ./examples/input/input.jpg --style_weight 1e3
```

### Other Options

`--style_option` specifies three different ways of style transferring. `--style_option 0` is to generate segmented intermediate result like torch file **neuralstyle_seg.lua** in torch. `--style_option 1` uses this intermediate result to generate final result like torch file **deepmatting_seg.lua**. `--style_option 2` combines these two steps as a one line command to generate the final result directly.

`--content_weight` specifies the weight of the content loss (default=5), `--style_weight` specifies the weight of the style loss (default=100), `--tv_weight` specifies the weight of variational loss (default=1e-3) and `--affine_weight` specifies the weight of affine loss (default=1e4). You can change the values of these weight and play with them to create different photos.

`--serial` specifies the folder that you want to store the temporary result **out_iter_XXX.png**. The default value of it is `./`. You can simply `mkdir result` and set `--serial ./result` to store them. **Again, the temporary results are simply clipping the image into [0, 255] without smoothing. Since for now, the smoothing operations need pycuda and pycuda will have conflict with tensorflow when using single GPU**

Run `python deep_photostyle.py --help` to see a list of all options

### Image Segmentation
This repository doesn't offer image segmentation script and simply use the segmentation image from the [torch version](https://github.com/luanfujun/deep-photo-styletransfer). The mask colors used are also the same as them. You could specify your own segmentation model and mask color to customize your own style transfer.


## Examples
Here are more results (from left to right are input, style, and result)

<p align="center">
    <img src='examples/input/input.jpg' height='162' width='300'/>
    <img src='examples/style/case1.jpg' height='162' width='270'/>
    <img src='some_results/Case1.png' height='162' width='300'/>
</p>

<p align="center">
    <img src='examples/input/in7.png' height='140' width='210'/>
    <img src='examples/style/tar7.png' height='140' width='210'/>
    <img src='examples/final_results/best7_t_1000.png' height='140' width='210'/>
    <img src='some_results/best7.png' height='140' width='210'/>
</p>

<p align="center">
    <img src='examples/input/in8.png' height='140' width='210'/>
    <img src='examples/style/tar8.png' height='140' width='210'/>
    <img src='examples/final_results/best8_t_1000.png' height='140' width='210'/>
    <img src='some_results/best8.png' height='140' width='210'/>
</p>

<p align="center">
    <img src='examples/input/in9.png' height='140' width='210'/>
    <img src='examples/style/tar9.png' height='140' width='210'/>
    <img src='examples/final_results/best9_t_1000.png' height='140' width='210'/>
    <img src='some_results/best9.png' height='140' width='210'/>
</p>

<p align="center">
    <img src='examples/input/in10.png' height='140' width='210'/>
    <img src='examples/style/tar10.png' height='140' width='210'/>
    <img src='examples/final_results/best10_t_1000.png' height='140' width='210'/>
    <img src='some_results/best10.png' height='140' width='210'/>
</p>

<p align="center">
    <img src='examples/input/in11.png' width='210'/>
    <img src='examples/style/tar11.png' width='210'/>
    <img src='examples/final_results/best11_t_1000.png' width='210'/>
    <img src='some_results/best11.png' width='210'/>
</p>

## Acknowledgement

* This work was done by Vien Bui, Jacob John Jeevan and Viren Viraj Shankar at *University of Alabama at Birmingam*.

* This repository is basically based on the [Tensorflow implementation](https://github.com/LouieYang/deep-photo-styletransfer-tf) of Deep Photo Styletransfer by Yang Liu.

## Contact
Feel free to contact me if there is any question (Vien Bui bnvien@gmail.com).
